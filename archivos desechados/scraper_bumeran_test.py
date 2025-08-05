from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
#options.add_argument("--headless")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.bumeran.com.ar/empleos-area-tecnologia-sistemas-y-telecomunicaciones.html"
driver.get(url)

# Nuevo método más general para esperar
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "h2"))
)

# Capturar screenshot
driver.save_screenshot("debug_final.png")

# Mostrar títulos de trabajos
titles = driver.find_elements(By.TAG_NAME, "h2")
for t in titles:
    print("🔹", t.text)

driver.quit()
