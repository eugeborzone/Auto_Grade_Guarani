from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

from Configuracion import *


driver = webdriver.Chrome(ChromeDriverManager().install())
# Preparo funciones de espera
def espera_corta(espera_corta = espera_corta):
    driver.implicitly_wait(espera_corta)
def espera_larga(espera_larga = espera_larga):
    driver.implicitly_wait(espera_larga)

# Navegar a la página de inicio de sesión
driver.get(url_login)
# maximizo
driver.maximize_window()
# Wait
espera_corta()

# Rellenar el formulario de inicio de sesión
usuario_input = driver.find_element(By.ID, 'usuario')
espera_corta()
usuario_input.send_keys(usuario)
espera_corta()
# Wait
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