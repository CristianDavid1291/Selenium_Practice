
import unittest
from selenium import webdriver
import time

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
        
        
        #driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
       

        
        
    def test1(self):  
        driver = self.driver
        driver.get("")
        self.driver.maximize_window()
        

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()