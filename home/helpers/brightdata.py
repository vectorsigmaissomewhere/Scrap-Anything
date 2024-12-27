url = "https://www.amazon.com/PlayStation-Store-Gift-Card-Digital/dp/B0CXBLK3WW/ref=sr_1_2?crid=JJE3LDTKV7I7&dib=eyJ2IjoiMSJ9.sbmLpE8_YAziJzrQsAP4zzdyJ5WQJhL3ddiGHhFskB9Zt2o3E9MfidruBEjeZ8xIbOs8y-IvA8zDXCFd7KJmlPdzRRmW94MCQOknXH4E3NgXVpdr1TLPMOyt83R6scPEhH04IxFHH54xftV4aHpdGtjgZIF1yYoSJj0fMnSfOA-15rLSjHONbjVyZDud62TZS-F3WlP8nPDPZ1O785H3nCMZvRiFbkI9NLSiGfh5Geg.Hf-oWEAvayLh5vxUiwWmh7q6_7A7TpSHI2P1xPAXZAM&dib_tag=se&keywords=ps5&qid=1735308458&sprefix=ps%2Caps%2C351&sr=8-2&th=1"

#!/usr/bin/env python3
from selenium.webdriver import Remote, ChromeOptions as Options
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection
from decouple import config 

# Replace 'USER:PASS' with the provided credentials
AUTH = "brd-customer-hl_38555767-zone-scraping_browser1:vp9d21s813bw"
TARGET_URL = 'https://www.amazon.com/PlayStation-Store-Gift-Card-Digital/dp/B0CXBLK3WW/'

def scrape(url=TARGET_URL):
    if AUTH == 'USER:PASS':
        raise Exception('Provide valid credentials in AUTH.')
    print('Connecting to Browser...')
    server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
    connection = Connection(server_addr, 'goog', 'chrome')
    driver = Remote(connection, options=Options())
    try:
        print(f'Connected! Navigating to {url}...')
        driver.get(url)
        print('Navigated! Scraping page content...')
        data = driver.page_source
        print(f'Scraped! Data: {data}')
    finally:
        driver.quit()

if __name__ == '__main__':
    scrape()