# Auto Grade Guaraní
### Sistema de cargado de notas automatico para SIU Guaraní



# Requerimientos
-Pandas

-Selenium

-bs4

# Funcionamiento
1) Editar el archivo Configuracion.py con sus parámetros personalizados. Seleccionar el sistema operativo con el parámetro so.
2) Las notas se esperan en un archivo notas.csv separado por comas (',') con dos columnas con dni y nota.
3) Ejecutar el archivo Auto_Grade.py
# Resetear Todo
Para hacer un reseteo de notas y condiciones a los valores vacíos por defecto ('-') solo se debe configurar en el archivo de Configuracion.py el parámetro reset_all=True
# Ir a página de notas
El archivo Go_to_notas_page.py realiza los pasos necesarios para llegar a la página de carga de notas. Esto es útil para depurar el código, para cambiar valores (xpath de botones, codificación de notas, etc) para diferentes versiones de SIU Guaraní. 
# Precauciones
Probado actualmente con el SIU Guaraní de UNL-FICH. Es posible que para otros haya que hacer ligeros cambios en los XPATH de los botones en el archivo Auto_Grade.py
# Licencia
Usted es libre de copiar y modificar lo que quiera de esta repo.

## Autores

Eugenio Borzone

Bruno Zorzet
