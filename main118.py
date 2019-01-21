# pylint: disable=E0401,E1121
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException,NoSuchElementException,StaleElementReferenceException,WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Instagram:
    def __init__(self):
        options = Options()
        #options.set_headless(headless=True)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.wait = WebDriverWait(self.driver, 0)
        self.urls = ["https://www.instagram.com/fearythanyarat/","https://www.instagram.com/wow_kimsohyun/?hl=vi","https://www.instagram.com/you_r_love/?hl=vi"]
    def colpic(self):
        for url in self.urls:
            self.__parse(url) 
        self.driver.close()
    def __parse(self,url):
        self.driver.get(url)
        self.driver.find_element_by_xpath('//div[@class="_9AhH0"]').click() #first click
        while True: #next loop
            try:
                nextpic = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="    coreSpriteRightChevron"]')))
                nextpic.click()
            except (TimeoutException, StaleElementReferenceException, WebDriverException):
                try:
                    nextstatus = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="HBoOv coreSpriteRightPaginationArrow"]')))
                    nextstatus.click()
                except TimeoutException:
                    break
        print("lets it begin")
if __name__ == "__main__":
    a = Instagram()
    a.colpic()

