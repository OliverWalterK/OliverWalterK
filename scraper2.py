from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import urllib.request
import time, uuid, urllib, os, requests, json

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
            loop = self.driver.find_elements(By. XPATH, "//a[@href]")
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
        '''This method will get price,name,link,uuid and pictures.'''
        self.dictionary = {
                    'UUID':[],
                    'Link':[],
                    'Name':[],
                    'Price':[]
                          }
        # url_list = []
        for links in self.valid_url[:5]:
            self.driver.get(links)
            time.sleep(2)
            try:
                value = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/main/div[3]/div[3]/div/div/div/span[1]/p[2]').text
                self.dictionary['Price'].append(value)
            except NoSuchElementException:
                self.dictionary['Price'].append('N/A')
            try:
                self.dictionary['Link'].append(links)
            except NoSuchElementException:
                self.dictionary['Link'].append('N/A')
            try:
                splitted = links.split("/")[-1]
                self.dictionary['Name'].append(splitted)
            except NoSuchElementException:
                self.dictionary['Name'].append('N/A')
            # try:
            #     find_picture_links = self.driver.find_elements(By. XPATH, "//img[@src]")
            #     for picture in find_picture_links:
            #         url_list.append(picture.get_attribute("src"))
            #     for url in url_list:
            #         r = requests.get(url)
            #         with open('/home/oliver/Desktop/AiCore/Application2/attempt2/raw_data/picture.jpg', 'wb+') as ex:
            #             ex.write(r.content)
            # except NoSuchElementException:
            #     print("No pictures were found.")
            links = str(uuid.uuid4())
            self.dictionary['UUID'].append(links)

    def make_json(self):
        with open('/home/oliver/Desktop/AiCore/Application2/attempt2/raw_data/data.json', 'w') as fp:
            json.dump(self.dictionary, fp)