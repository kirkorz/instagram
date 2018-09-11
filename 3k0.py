from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class doit:
    start_urls = ["https://www.instagram.com/wow_kimsohyun/"]

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        user = self.driver.find_elements_by_xpath("//input[@class='_2hvTZ pexuQ zyHYP']")
        user[0].send_keys("kkikko512")
        ActionChains(self.driver).send_keys(Keys.TAB + "tuki***codon123" + Keys.ENTER).perform()
        time.sleep(3)
        
    def getimg(self):
        li =list()
        for link in self.start_urls:
            self.driver.get(link)
        check_height = self.driver.execute_script("return document.body.scrollHeight;")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                pg = self.driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a")
                for p in [-i for i in range(1,13)]:
                    li.append(pg[p].get_attribute('href'))
                self.wait.until(lambda driver: self.driver.execute_script("return document.body.scrollHeight;")  > check_height)
                check_height = self.driver.execute_script("return document.body.scrollHeight;")
            except TimeoutException:
                print("het gio ------------------------")
                break

        for l in set(li):
            print(l)
        print("done")

    def unfollow(self):
        self.driver.get(self.start_urls[0])
        self.driver.execute_script("document.body.getElementsByClassName('Szr5J kIKUG coreSpriteDesktopNavProfile')[0].click()")
        time.sleep(3)
        #self.driver.execute_script("document.body.getElementsByClassName(' _81NM2')[1].click()")
        
        
        
        
        check_height = self.driver.execute_script("return document.body.getElementsByClassName('j6cq2')[0].scrollHeight;")
        
        while True:
            self.driver.execute_script("document.body.getElementsByClassName('j6cq2')[0].scrollTo(0, document.body.getElementsByClassName('j6cq2')[0].scrollHeight);")
            time.sleep(3)
            try:
                self.wait.until(lambda driver: self.driver.execute_script("return document.body.getElementsByClassName('j6cq2')[0].scrollHeight;")  > check_height)
                
                check_height = self.driver.execute_script("return document.body.getElementsByClassName('j6cq2')[0].scrollHeight;")
                
            except TimeoutException:
                print("het gio ------------------------")
                break

    def parse(self):
        li = list()
        for link in self.start_urls:
            self.driver.get(link)

        click = self.driver.find_elements_by_xpath("//a[@class='-nal3 ']") 
        ActionChains(self.driver).move_to_element(click[1]).click().perform()
        

        #fol = self.driver.find_elements_by_xpath("//div[@class='Pkbci']/button")
        #print(fol)
        #ActionChains(self.driver).move_to_element(fol[0]).click().perform()
        #ActionChains(self.driver).move_to_element(fol[0]).perform()

        #sc = self.driver.find_elements_by_xpath("//div[@class='j6cq2']")
        #print(sc)
        #ActionChains(self.driver).move_to_element(sc[0]).perform()

        time.sleep(3)#XXXX
        


        check_height = self.driver.execute_script("return document.body.getElementsByClassName('j6cq2')[0].scrollHeight;")
        time.sleep(3)
        n = 1
        while True:
            self.driver.execute_script("document.body.getElementsByClassName('j6cq2')[0].scrollTo(0, document.body.getElementsByClassName('j6cq2')[0].scrollHeight);")
            time.sleep(3)
            try:
                fol = self.driver.find_elements_by_xpath("//div[@class='Pkbci']/button")
                [ActionChains(self.driver).move_to_element(al).click().perform() for al in [fol[i] for i in range(n-1,12*n-1)]]
                n = n + 1
                if n > 40:
                    break
                self.wait.until(lambda driver: self.driver.execute_script("return document.body.getElementsByClassName('j6cq2')[0].scrollHeight;")  > check_height)
                time.sleep(3)
                check_height = self.driver.execute_script("return document.body.getElementsByClassName('j6cq2')[0].scrollHeight;")
                time.sleep(3)
            except TimeoutException:
                print("het gio ------------------------")
                break


        check_height = self.driver.execute_script("return document.body.scrollHeight;")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                pg = self.driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']/a")
                for p in [-i for i in range(1,13)]:
                    li.append(pg[p].get_attribute('href'))
                self.wait.until(lambda driver: self.driver.execute_script("return document.body.scrollHeight;")  > check_height)
                check_height = self.driver.execute_script("return document.body.scrollHeight;")
            except TimeoutException:
                print("het gio ------------------------")
                break

        
        
        for l in set(li):
            print(l)
        print("done")

    def p2(self):
        self.parse(self.start_urls)

if __name__ == "__main__":
    a = doit()
    a.login()
    a.unfollow()




