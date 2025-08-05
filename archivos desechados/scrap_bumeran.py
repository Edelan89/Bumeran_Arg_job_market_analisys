# Import the frameworks i will use
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up Chrome in headless mode
options = Options()
options.add_argument('--headless') # Run in headless mode
options.add_argument('--no--sandbox') # Bypass OS security model
options.add_argument('--disable-dev-shm-usage') # Overcome limited resource problems

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Initial parameters
base_url = "https://www.bumeran.com.ar/empleos-area-tecnologia-sistemas-y-telecomunicaciones.html?page={}"
#headers = {
#    "User-Agent": "Mozilla/5.0"
#}

# list to store the job data
job_list = []

# Loop through the first 3 pages
for page in range(1,4):
    url = base_url.format(page)
    print(f'Scraping page {page}...')
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
#    response = requests.get(url, headers=headers)
#    soup = BeautifulSoup(response.content, 'html.parser')

    # Each job is contained in an "article" tag with an specific class
#    offers = soup.find_all('article')

    jobs = driver.find_elements(By.TAG_NAME, 'article')

    for job in jobs:
        try:
            title = job.find_element(By.TAG_NAME,"h2").text
        except:
            title = "No title found"
        try:
            company = job.find_element(By.CLASS_NAME, "sc-1ojbivn-4").text
        except:
            company = "No company found"
        try:
            location = job.find_element(By.CLASS_NAME, "sc-1ojbivn-8").text
        except:
            location = "No location found"
        try:
            published = job.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        except:
            published = "No date found"
        try:
            link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = "No link found"

        job_list.append({
            "title":title,
            "company":company,
            "location":location,
            "published_date":published,
            "link":link
        })
    
    driver.quit() # Close the driver after scraping each page 
    #time.sleep(2)  # Sleep to avoid overwhelming the server

# Create a DataFrame from the job list
df = pd.DataFrame(job_list)
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('bumeran_jobs.csv', index=False)