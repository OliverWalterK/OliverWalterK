from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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
        self.all_url = []
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href]")))
            loop = self.driver.find_elements_by_xpath("//a[@href]")
            for links in loop:
                self.all_url.append(links.get_attribute("href"))
        except:
            print("No links found. Website might not have loaded correctly. Try again.")
        return self.all_url

    def valid_links(self):
        '''Aims to clean the list (all_url) and get the relevant links (valid_url).'''
        self.valid_url = []
        for i in self.all_url:
            if "trade" and "-" in i:
                self.valid_url.append(i)
        del self.valid_url[-5:]
        del self.valid_url[:2]
        return self.valid_url

    def get_data(self):
        '''This method will get data such as price,name,link,uuid and create a dictionary.'''
        dictionary = {
                    'UUID':[],
                    'Link':[],
                    'Name':[],
                    'Price':[]
                    }
        for links in self.valid_url:
            self.driver.get(links)
            time.sleep(2)
            try:
                value = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/main/div[3]/div[3]/div/div/div/span[1]/p[2]").text
                dictionary['Price'].append(value)
            except NoSuchElementException:
                dictionary['Price'].append('N/A')
            try:
                dictionary['Link'].append(links)
            except NoSuchElementException:
                dictionary['Link'].append('N/A')
            try:
                splitted = links.split("/")[-1]
                dictionary['Name'].append(splitted)
            except NoSuchElementException:
                dictionary['Name'].append('N/A')
            links = str(uuid.uuid4())
            dictionary['UUID'].append(links)