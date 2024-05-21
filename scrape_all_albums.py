import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from docx import Document

# Update this path to the location of your chromedriver executable
CHROME_DRIVER_PATH = '/Users/elizabethearhart/Downloads/chromedriver-mac-x64/chromedriver'

def scrape_and_save(url):
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    driver.get(url)
    wait.until(EC.presence_of_all_elements_located)

    # Create a list to store scraped data
    scraped_data = []

    span_elements = driver.find_elements(By.CLASS_NAME, "tK8GG")
    for span_element in span_elements:
        node_value = span_element.text
        scraped_data.append(node_value)

    # Export data to Word document
    doc = Document()
    for data in scraped_data:
        doc.add_paragraph(data)
    doc.save('album_data_{}.docx'.format(url.split('/')[-1]))

    # Close the browser
    driver.quit()

# List of URLs to scrape
urls = [
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/fearless-taylors-version-chords-5069464",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/evermore-chords-5107186",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/folklore-chords-5102914",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/lover-chords-2805578",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/midnights-chords-4887437",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/red-taylors-version-chords-5072530",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/speak-now-taylors-version-chords-4863422",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/taylor-swift-chords-865964",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/the-tortured-poets-department-chords-5233998"
    # Add more URLs here
]

# Scrape each URL
for url in urls:
    scrape_and_save(url)
