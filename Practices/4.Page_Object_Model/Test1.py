from pyclbr import Function
import unittest
from selenium import webdriver
import time
from Functions.Login_Page import Login_Page
from Functions.Functions import Functions




class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
        #driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
         
        
    def test1(self):  
      pg = Login_Page(self.driver)  
      pg.main_process_login_page()

    def test2(self):
        f=Functions(self.driver)
        f.navigate("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        f.select_xpath_index(10,"//select[@id='select-demo']",2,3)
    
    def test3(self):
        f=Functions(self.driver)
        f.navigate("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
        f.check_xpath_multiple(.4,"//label[contains(.,'Option')]")
        

    def tearDown(self):
        driver = self.driver
        driver.close()

    

if __name__ == '__main__':
    unittest.main()