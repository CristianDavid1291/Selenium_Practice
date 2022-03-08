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
        path = ".\\Practices\\5.Excel_Practice\\Excel_Functions\\Data.xlsx"
        rows = excelFunction.getCountRow(path=path,sheetName="Hoja1")
        for i in range(2,rows+1):
            name = excelFunction.readData(path=path,sheetName="Hoja1",numRow=i,numColum=1)
            email = excelFunction.readData(path=path,sheetName="Hoja1",numRow=i,numColum=2)
            address = excelFunction.readData(path=path,sheetName="Hoja1",numRow=i,numColum=3)
            address2 = excelFunction.readData(path=path,sheetName="Hoja1",numRow=i,numColum=4)

            f.text_xpath_validate("//input[@id='userName']",name,2,2)
            f.text_xpath_validate("//input[@id='userEmail']",email,2,2)
            f.text_xpath_validate("//textarea[@id='currentAddress']",address,2,2)
            f.text_xpath_validate("//textarea[@id='permanentAddress']",address2,2,2)
            f.text_xpath_validate_click("//button[@id='submit']",2,2)

            if(f.exist("id","name",2)):
                excelFunction.writeData(path,"Hoja1",i,5,"Insertado")
            else:
                excelFunction.writeData(path,"Hoja1",i,5,"Error")
               


 
        

    def tearDown(self):
        driver = self.driver
        driver.close()

    

if __name__ == '__main__':
    unittest.main()