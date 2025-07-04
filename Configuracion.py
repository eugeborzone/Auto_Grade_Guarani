# Definir las credenciales de inicio de sesión
#load dotenv
import os
from dotenv import load_dotenv
load_dotenv()
# tomar usuario y contraseña del archivo .env
usuario = os.getenv('usuario')
contraseña = os.getenv('contraseña')

# Definir url de inicio de sesión de tu SIU Guaraní
url_login = 'https://servicios.unl.edu.ar/guarani3/autogestion/acceso'
# Definir XPath de la materia
xpath_materia = '//a[@data-original-title="" and text()="Introducción a la Inteligencia Artificial"]'
# path a csv con la notas, separados por coma (',') con las columnas dni y nota
path_notas = 'notas.csv'

# definir rangos de notas para definir el estado de la materia nota=0 se considera ausente
notas_libre = [1,2,3,4,5]
notas_no_promocionan = [6,7]
notas_promocionan = [8,9,10]
# definir el estado de la materia en función de la nota
condicion_cursada = {'Abandono': 'Abandono',
                    'Libre': 'Libre', 
                    'Regular': 'Regular', 
                    'Promocionado': 'Regular'}
resultado_promocion =  {'Abandono': 'Ausente',
                        'Libre': 'No Promocionado', 
                        'Regular': 'No Promocionado', 
                        'Promocionado': 'Promocionado'}

# definir cuantas paginas tiene el listado de alumnos
numero_paginas = 11

# definir tiempo de espera para que cargue la pagina (aumentar si la conexión es lenta)
espera_corta = 5
espera_larga = 20

# parametro para resetear las notas y las condiciones de los alumnos 
reset_all = False

# so
so = 'Windows'

