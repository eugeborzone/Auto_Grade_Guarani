# Auto Grade Guaraní
### Sistema de cargado de notas automatico para SIU Guaraní



# Requerimientos
-Pandas

-Selenium

-webdriver_manager

-bs4

# Funcionamiento
1) Editar el archivo Configuracion.py con sus parámetros personalizados. Seleccionar el sistema operativo con el parámetro so.
2) Guardar las notas a subir en un archivo .csv separado por comas (',') con dos columnas con nombre dni y nota.
3) Ejecutar el arhivo Auto_Grade.py
# Resetear Todo
Para hacer un reseteo de notas y condiciones a los valores vacios por defecto ('-') solo se debe configurar en el archivo de Configuracion.py el parametro reset_all=True
# Precauciones
Probado actualmente con el SIU Guaraní de UNL-FICH. Es posible que para otros haya que hacer ligeros cambios en los XPATH de los botones en el archivo Auto_Grade.py
