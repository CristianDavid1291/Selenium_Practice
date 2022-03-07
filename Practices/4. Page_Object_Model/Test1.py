import unittest
from selenium import webdriver
import time
from Functions.Functions import Functions




class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
        #driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
         
        
    def test1(self):  
        driver = self.driver
        f = Functions(driver)
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        f.time(5)
        

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()