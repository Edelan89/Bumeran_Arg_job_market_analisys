from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

# In this version of the script, I scrape all job offers from Bumeran Argentina, not just in the technology sector.

# Configuración Selenium
options = Options()
#options.add_argument("--headless")  # Activá si después querés
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

all_jobs = []

# Elegí cuántas páginas querés scrapear
total_pages = 690 

for page in range(1, total_pages + 1):
    if page == 1:
        url = "https://www.bumeran.com.ar/empleos.html"
    else:
        url = f"https://www.bumeran.com.ar/empleos.html?page={page}"
    
    print(f"Scrapeando página {page} - URL: {url}")
    driver.get(url)
    time.sleep(10)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_links = soup.find_all("a", href=lambda href: href and "/empleos/" in href)

    for link in job_links:
        try:
            href = "https://www.bumeran.com.ar" + link["href"]
            title_tag = link.find("h2")
            title = title_tag.text.strip() if title_tag else "No disponible"

            parent = link.find_parent("div")

            # Empresa
            company = "No disponible"
            h3_tags = parent.find_all("h3")
            for h3 in h3_tags:
                if "Publicado" not in h3.text:
                    company = h3.text.strip()
                    break

            # Ubicación
            location = "No disponible"
            icon = parent.find("i", attrs={"name": "icon-light-location-pin"})
            if icon:
                sibling_span = icon.find_next_sibling("span")
                if sibling_span:
                    h3 = sibling_span.find("h3")
                    if h3:
                        location = h3.text.strip()

            all_jobs.append({
                "Puesto": title,
                "Empresa": company,
                "Ubicación": location,
                "Link": href
            })
        except Exception as e:
            print(f"Error en una oferta de la página {page}: {e}")
            continue

driver.quit()

# Exportamos resultados
df = pd.DataFrame(all_jobs)
print(df.head(10))
print(f"Total de ofertas encontradas: {len(df)}")

df.to_csv("bumeran_jobs_general.csv", index=False)
