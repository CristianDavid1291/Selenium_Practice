from pyclbr import Function
import unittest
from selenium import webdriver
import time
from Excel_Functions.Exc_Functions import Excel_Functions
from Excel_Functions.Functions import Functions



class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
        #driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
         
        
    def test1(self):
        f=Functions(self.driver)
        excelFunction =  Excel_Functions(self.driver)
        f.navigate(path="https://demoqa.com/text-box")
        path = "F:\CRISTIAN\Cursos\Selenium\Practices\5.Excel_Practice\Test1_Excel.py"

 
        

    def tearDown(self):
        driver = self.driver
        driver.close()

    

if __name__ == '__main__':
    unittest.main()