#first make sure you have installed google chrome and the appropriate driver
#import necessary libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from docx import Document

# Update this path to the location of your chromedriver
CHROME_DRIVER_PATH = '/Users/eearhart/Downloads/chromedriver-mac-x64/chromedriver'

#instruct selenium to use google chrome driver to access the given url
def scrape_and_save(url):
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    #I used webdriver wait to make sure all of the elements on the page were loaded, because ultimate-guitar is very slow
    driver.get(url) 
    wait.until(EC.presence_of_all_elements_located)

    # Create a list to store scraped data and specify the elements to be scraped by locating them in the website's html
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

    # Close browser
    driver.quit()

# Specify each url that should be scraped, in this case all album entires.
urls = [
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/taylor-swift-chords-865964",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/fearless-taylors-version-chords-5069464",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/speak-now-taylors-version-chords-4863422",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/red-taylors-version-chords-5072530",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/1989-chords-1674195"
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/reputation-chords-2241303"
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/lover-chords-2805578",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/folklore-chords-5102914",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/evermore-chords-5107186",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/midnights-chords-4887437",
    "https://tabs.ultimate-guitar.com/tab/taylor-swift/the-tortured-poets-department-chords-5233998"
]

# Scrape all URLs
for url in urls:
    scrape_and_save(url)
