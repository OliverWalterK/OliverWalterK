from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time, uuid, urllib, os, requests

class Scraper:
    def __init__(self, url, options=None):
        self.url = url
        if options:
            self.driver = Chrome(ChromeDriverManager().install(), options=options)
        else:
            self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(self.url)
    
    def find_all_links(self):
        '''Finds elements on website with //a[@href] and compiles a list called (all_url)'''
        all_url = []
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href]")))
            loop = self.driver.find_elements_by_xpath("//a[@href]")
            for links in loop:
                all_url.append(links.get_attribute("href"))
        except:
            print("No links found. Website might not have loaded correctly. Try again.")
        return all_url

    def valid_links(self, all_url):
        '''Aims to clean the list (all_url) and get the relevant links (valid_url)'''
        valid_url = []
        for i in all_url:
            if "trade" and "-" in i:
                valid_url.append(i)
        del valid_url[-5:]
        del valid_url[:2]
        return valid_url

    def get_data(self):
        