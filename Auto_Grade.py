from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

from Configuracion import *


# Abrir el navegador
driver = webdriver.Chrome(ChromeDriverManager().install())
# Configurar las opciones del navegador
driver.get(url_login)
# maximizo
driver.maximize_window()

# Proceso datos de entrada

# Preparo funciones de espera
def espera_corta(espera_corta = espera_corta):
    driver.implicitly_wait(espera_corta)
def espera_larga(espera_larga = espera_larga):
    driver.implicitly_wait(espera_larga)

# leer los datos de las notas de csv con pandas
notas = pd.read_csv(path_notas, sep=',')
# transformo la columna nota a tipo int
notas['nota'] = notas['nota'].astype(int)

# codigos de condiciones de cursada y promoción en SIU Guaraní (ver en la página de carga de notas)
condiciones_cursada_SIU = { '-': '', 'Abandono': '2', 'Insuficiente': '3', 'Libre': '1', 'Libre x Inasistencia': '100',
                         'Regular': '4', 'Regularidad Incompleta': '122', 'Renuncia': '120'}
resultados_promocion_SIU = {'-': '', 'Ausente': 'U', 'No Promocionado': 'R', 'Promocionado': 'A'}
if reset_all:
    condicion_cursada = {'Abandono': '-',
                    'Libre': '-', 
                    'Regular': '-', 
                    'Promocionado': '-'}
    resultado_promocion =  {'Abandono': '-',
                            'Libre': '-', 
                            'Regular': '-', 
                            'Promocionado': '-'}
# cambio los valores de las condiciones por los valores internos del SIU
condicion_cursada = {k: condiciones_cursada_SIU[v] for k, v in condicion_cursada.items()}
resultado_promocion = {k: resultados_promocion_SIU[v] for k, v in resultado_promocion.items()}

espera_corta()

# Rellenar el formulario de inicio de sesión
usuario_input = driver.find_element(By.ID, 'usuario')
espera_corta()
usuario_input.send_keys(usuario)
espera_corta()
contraseña_input = driver.find_element(By.ID, 'password')
espera_corta()
contraseña_input.send_keys(contraseña)
espera_corta()
contraseña_input.send_keys(Keys.RETURN)  # Presionar Enter para enviar el formulario
espera_corta()

# Redireccionar a la página de comisiones
element = driver.find_element(By.ID, 'zona_comisiones')
element.click()
# Redireccionar a la página de la materia
elemento = driver.find_element(By.XPATH, xpath_materia)
elemento.click()
# Redireccionar a la página de carga de notas
elemento = driver.find_element(By.XPATH, '//*[@id="zona"]/div[1]/ul[2]/li[2]/a')
elemento.click()
espera_larga()


# Recorro las paginas de alumnos
for page in range(numero_paginas):
    
    # Coloco la fecha de hoy
    element = driver.find_element(By.ID, 'js-colapsar-herramientas')
    espera_corta()
    element.send_keys(Keys.RETURN) 
    espera_corta()
    campo_select = Select(driver.find_element(By.ID, 'preset_campo'))
    espera_corta()
    campo_select.select_by_value('fecha')
    espera_corta()
    campo_select = driver.find_element(By.ID, 'preset-fecha')
    espera_corta()
    campo_select.send_keys(time.strftime('%d/%m/%Y')) 
    espera_corta()
    campo_select.send_keys(Keys.RETURN)
    espera_corta()
    boton = driver.find_element(By.ID, 'btnCompletar')
    espera_corta()
    boton.click()

    # Genero listas a recorrer
    
    # Obtenemos los id de las clases de regularización:
    # Encontrar los elementos que pertenecen a la clase específica
    elementos_regularizacion = driver.find_elements(By.CLASS_NAME, 'js-renglon-regular')
    # Recuperar los IDs de los elementos
    ids_regularizacion = [elemento.get_attribute('id') for elemento in elementos_regularizacion]
    
    # Obtenemos los id de las clases de promocion:
    # Encontrar los elementos que pertenecen a la clase específica
    elementos_promocion = driver.find_elements(By.CLASS_NAME, 'js-renglon-promocion')
    # Recuperar los IDs de los elementos
    ids_promocion = [elemento.get_attribute('id') for elemento in elementos_promocion]

    # Obtengo los elementos de las notas y condiciones de cursada
    notas_cursada = driver.find_elements(By.CLASS_NAME, 'nota_cursada')
    condicion_cursada = driver.find_elements(By.CLASS_NAME, 'condicion')
    # Obtengo los elementos de los resultados de promoción
    resultado_promocion = driver.find_elements(By.CLASS_NAME, 'resultado')
    notas_promocion = driver.find_elements(By.CLASS_NAME, 'nota_promocion')

    # Obtengo el html de la página para buscar los dni de los alumnos para comprobar que nota tienen
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    for i,id_ in enumerate(ids_regularizacion):

        # obtengo el dni del alumno
        renglon = soup.find('tr', id=id_)
        dni_span = renglon.find('span', class_='identificacion')
        dni = dni_span.text.split(' ')[1]

        #combrobar nota
        #busco la nota por dni
        if len(notas.loc[notas['dni'] == int(dni), 'nota'].values) == 0:
            nota = 0
        else:
            nota = notas.loc[notas['dni'] == int(dni), 'nota'].values[0]

        if nota == 0: 
            # Cursada - Abandono
            campo_select = Select(condicion_cursada['Abandono'])
            espera_corta()
            campo_select.select_by_value(condicion_cursada['Abandono'])
            espera_corta()
            # Promocion - Abandono
            campo_select = Select(driver.find_elements(By.NAME, f'renglones[{id_[8:]}][resultado_promocion]')[0])
            espera_larga()
            campo_select.select_by_value(resultado_promocion['Abandono'])
            espera_corta()

        elif nota in notas_libre:
            # Cursada - Libre
            campo_select = Select(condicion_cursada[i])
            espera_corta()
            campo_select.select_by_value(condicion_cursada['Libre'])
            espera_corta()

            # Promocion - Libre
            campo_select = Select(driver.find_elements(By.NAME, f'renglones[{id_[8:]}][resultado_promocion]')[0])
            espera_larga()
            campo_select.select_by_value(resultado_promocion['Libre'])
            espera_corta()

        elif nota in notas_no_promocionan:
            # Cursada - Regular
            campo_select = Select(condicion_cursada[i])
            espera_corta()
            campo_select.select_by_value(condicion_cursada['No promocionado'])
            espera_corta()

            # Promocion - Regular
            campo_select = Select(driver.find_elements(By.NAME, f'renglones[{id_[8:]}][resultado_promocion]')[0])
            espera_larga()
            campo_select.select_by_value(resultado_promocion['No promocionado'])
            espera_corta()

        else:
            # Cursada - Promociona
            campo_select = Select(condicion_cursada[i])
            espera_corta()
            campo_select.select_by_value(condicion_cursada['Promocionado'])
            espera_corta()
            # Promocion - Promociona
            campo_select = Select(notas_promocion[i])
            espera_corta()
            campo_select.select_by_value(str(nota))
            espera_corta()
        
    
    # guardo notas
    espera_larga()
    elemento = driver.find_element(By.XPATH, '//*[@id="renglones"]/form/div/input')
    elemento.click()

    # Cambiar de pagina
    # solicito url actual
    url = driver.current_url
    # cambio el numero de pagina
    if page == 0:
        url = url + '/' + str(page+2)
        # redirecciono
        driver.get(url)
    elif page == numero_paginas-1:
        pass
    else:
        url = url[:-1] + str(page+2)
        # redirecciono
        driver.get(url)
        
    espera_larga()