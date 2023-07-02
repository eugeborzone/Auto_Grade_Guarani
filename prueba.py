from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Configura el controlador de Chrome utilizando webdriver_manager

# Abre una página web
driver.get('https://www.example.com')

# Realiza acciones en la página
# ...

# Cierra el navegador
driver.quit()