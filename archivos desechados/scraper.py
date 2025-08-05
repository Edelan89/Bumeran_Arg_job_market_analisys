from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

# Configuration of Selenium WebDriver
options = Options()
# The headless is not working properly with the current setup, so I won't use it for now.
#options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

print("Loading page...")
url = "https://www.bumeran.com.ar/empleos-area-tecnologia-sistemas-y-telecomunicaciones.html"
driver.get(url)
# Using 5 seconds, doesn't work properly, so I will use 10 seconds.
time.sleep(10)

print("Scraping job from the page...")
soup = BeautifulSoup(driver.page_source, "html.parser")

# Search for job links
job_links = soup.find_all("a", href=lambda href: href and "/empleos/" in href)

# List to store job data
jobs = []

# Iterate over each job link to extract details
for link in job_links:
    try:
        href = "https://www.bumeran.com.ar" + link["href"]
        title_tag = link.find("h2")
        title = title_tag.text.strip() if title_tag else "No disponible"

        parent = link.find_parent("div")

        # Company: Looking for h3 that is in the same container as the title (usually after the title)
        company = "No disponible"
        h3_tags = parent.find_all("h3")
        for h3 in h3_tags:
            if "Publicado" not in h3.text:
                company = h3.text.strip()
                break

        # locantion: Search for the <i> with name="icon-light-location-pin" and then go to its sibling <span>
        location = "No disponible"
        icon = parent.find("i", attrs={"name": "icon-light-location-pin"})
        if icon:
            sibling_span = icon.find_next_sibling("span")
            if sibling_span:
                h3 = sibling_span.find("h3")
                if h3:
                   location = h3.text.strip()


        jobs.append({
            "Puesto": title,
            "Empresa": company,
            "Ubicación": location,
            "Link": href
        })
    except Exception as e:
        print(f"Error en una oferta: {e}")
        continue

driver.quit()

df = pd.DataFrame(jobs)
print(df.head(10))

# Guardar en CSV
df.to_csv("bumeran_jobs_gpt.csv", index=False)
