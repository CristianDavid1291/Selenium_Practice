import unittest
from selenium import webdriver
import time
from Functions.Login_Page import Login_Page




class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
        #driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
         
        
    def test1(self):  
      pg = Login_Page(self.driver)  
      pg.main_process_login_page()
        

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()