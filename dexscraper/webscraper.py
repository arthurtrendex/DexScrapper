from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import Driver
import sys

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = Driver(uc=True, undetectable=True, headless2=True)
        self.data = None

    def scrape(self):
        self.driver.get(self.url)
        self.table = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ds-dex-table")))
        links= self.table.find_elements(By.TAG_NAME, "a")
        for link in links:
            link_text = link.get_attribute("href")
            if link_text:
                link_text = link_text.replace("'", '"')
        all_links = [link.get_attribute("href") for link in links]
        data = self.table.text.split('\n')[13:]
        self.data = all_links, data

    def get_data(self):
        return self.data

    def close(self):
        self.driver.quit()
        
arguments = sys.argv
url = arguments[1]
scraper = WebScraper(url)
scraper.scrape()
data = scraper.get_data()
scraper.close()
print(data)
sys.exit(0)