from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import shutil
from bs4 import BeautifulSoup
import pandas as pd

# set up Chrome options (headless mode for not opening a browser window)
options = Options()
#options.add_argument("--headless") # Run in headless mode
options.add_argument("--start-maximized") # Start the browser maximized
#options.add_argument("--no-sandbox") # Bypass OS security model
#options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36") # Set a user agent

# Especify the path to the ChromeDriver executable
chrome_path = shutil.which("chrome") or shutil.which("chrome.exe")
if not chrome_path:
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

options.binary_location = chrome_path

print("Initializing Chrome driver...")

# Initialize the Chrome browser with ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Load the page
url = "https://www.bumeran.com.ar/empleos-area-tecnologia-sistemas-y-telecomunicaciones.html"
print("Loading page...")
driver.get(url)

# Wait, at least, one article have been loaded
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))

# Wait for the page to load
#time.sleep(10) 
driver.save_screenshot("debug_final.png") # Save a screenshot for debugging

#job_elements = driver.find_elements(By.TAG_NAME, "h2")
#job_cards = driver.find_elements(By.XPATH, "//article")

titles = driver.find_elements(By.TAG_NAME, "h2")

# Seeking elements of the job
print('Scraping job from the page...')

# Seek all offers jobs
#job_cards = soup.find_all("div", class_="sc-iNvWbf fEUNZF sc-cOoQYZ dhcAnX")
# seek offers by tag article
#job_cards = driver.find_elements(By.TAG_NAME, "h2")
#if not job_cards:
#    print('No job cards found, is the HTML structure different?')

#print(f"Se encontraron {len(job_cards)} ofertas.")

# list to store job details
jobs = []

for t in titles:
    try:
        title = t.text.strip()
        # go up in the DOM to find the container father wich has the job details
        parent = t.find_element(By.XPATH, "./ancestor::article")

        try: 
            company_elem = parent.find_element(By.TAG_NAME, "h3")
            company = company_elem.text.strip()
        except:
            company = "No company specified"

        try:
            location_elem = parent.find_element(By.XPATH, ".//div[contains(@class, 'sc-kixGy')]")
            location = location_elem.text.strip()
        except:
            location = "No location specified"
        
        try:
            published_elem = parent.find_element(By.XPATH, './/h3[contains(@class, "sc-xmbAS")]')
            published = published_elem.text.strip()
        except:
            published = "No date specified"
        
        try:
            link_elem = parent.find_element(By.TAG_NAME, "a")
            link = link_elem.get_attribute("href")
        except:
            link = "No link available"

        if title:
            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "published": published,
                "link": link
                })

    except Exception as e:
        print(f"Error processing job card: {e}")
#jobs = driver.find_elements(By.CLASS_NAME, "card-body")
# Let's try a different strategy, because seek by class name is not working.
# I will use XPath to find the job cards
#jobs = driver.find_elements(By.XPATH, "//article")

#if not jobs:
#    print('No jobs found, is the html different?')  

#for i, job in enumerate(jobs[:10], 1): # show the first 10 jobs
#    try:
#        title = job.find_element(By.TAG_NAME, 'h2').text
#        company = job.find_element(By.XPATH, ".//span[contains(text(),'Empresa')]").text
#        print(f"{i}. {title} - {company}")
#    except Exception as e:
#        print(f'{i}. Error retrieving job details: {e}')

driver.quit()

df = pd.DataFrame(jobs)
print(df.head())  # Show the first few rows of the DataFrame