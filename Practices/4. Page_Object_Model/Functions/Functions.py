from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Functions():

    def __init__(self,driver):
        self.driver = driver
    
    def time(self,time2):
        time.sleep(time2)
        

    def navigate(self,path):
      self.driver.get(path)
      self.driver.maximize_window()

    def text_xpath(self,xpath,text,time2):
        val=self.driver.find_element_by_xpath(xpath)
        val.clear()
        val.send_keys(text)
        time.sleep(time2)

    def text_xpath_validate(self,xpath,text,time2,time3):

        try:
            val = WebDriverWait(self.driver, time2).until(EC.element_to_be_clickable((By.XPATH,xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val.clear()
            val.send_keys(text)
            time.sleep(time3)
        except TimeoutException as ex:
            print(ex.msg)
            print("Element not found" + xpath)  

    def text_xpath_validate_click(self,xpath,time2,time3):

        try:
            val = WebDriverWait(self.driver, time2).until(EC.element_to_be_clickable((By.XPATH,xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val.click()
            time.sleep(time3)
        except TimeoutException as ex:
            print(ex.msg)
            print("Element not found" + xpath) 

    def select_xpath_index(self,time2,xpath,index,time3): 

        try:
            val = WebDriverWait(self.driver, time2).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = Select(val)
            val.select_by_index(index)
            time.sleep(time3)
        except TimeoutException as ex:
            print(ex.msg)
            print ("Select Element not found")

    def check_xpath_multiple(self,time2,xpath):
        vecElement = WebDriverWait(self.driver, time2).until(EC.visibility_of_all_elements_located((By.XPATH,xpath)))
        
        try:
            for i in vecElement:
                vecElement[i].click()
                time.sleep(time2)
        except TimeoutException as ex:
           for i in vecElement:
                print(ex.msg)
                print ("Select Element not found:"+ str(i))    

       


