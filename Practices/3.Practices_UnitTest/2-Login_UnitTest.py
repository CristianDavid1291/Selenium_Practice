
import unittest
from selenium import webdriver
import time

class Login_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
        
        
        #driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
           
    def test_login1(self):  
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        user_name=driver.find_element_by_xpath("//input[@id='user-name']")
        password=driver.find_element_by_xpath("//input[@id='password']")
        login_button=driver.find_element_by_xpath("//input[@id='login-button']")

        user_name.send_keys("Cristian")
        password.send_keys("1234")
        login_button.click()
        error = driver.find_element_by_xpath("//h3[@data-test='error']")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Username and password do not match any user in this service"):
            print("Incorrect data")
            print("Test1 ok")
        time.sleep(2)

    def test_login2(self):  
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        user_name=driver.find_element_by_xpath("//input[@id='user-name']")
        password=driver.find_element_by_xpath("//input[@id='password']")
        login_button=driver.find_element_by_xpath("//input[@id='login-button']")

        user_name.send_keys("")
        password.send_keys("1234")
        login_button.click()
        error = driver.find_element_by_xpath("//h3[@data-test='error']")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Username is required"):
            print("Name is missing: correct message")
            print("Test2 ok")
        time.sleep(2)  

    def test_login3(self):  
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        user_name=driver.find_element_by_xpath("//input[@id='user-name']")
        password=driver.find_element_by_xpath("//input[@id='password']")
        login_button=driver.find_element_by_xpath("//input[@id='login-button']")

        user_name.send_keys("Cristian")
        password.send_keys("")
        login_button.click()
        error = driver.find_element_by_xpath("//h3[@data-test='error']")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Password is required"):
            print("Password is missing: correct message")
            print("Test2 ok")
        time.sleep(2)   

    def test_login4(self):  
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        user_name=driver.find_element_by_xpath("//input[@id='user-name']")
        password=driver.find_element_by_xpath("//input[@id='password']")
        login_button=driver.find_element_by_xpath("//input[@id='login-button']")

        user_name.send_keys("")
        password.send_keys("")
        login_button.click()
        error = driver.find_element_by_xpath("//h3[@data-test='error']")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Username is required"):
            print("Epic sadface: Username is required: correct message")
            print("Test2 ok")
        time.sleep(2) 

    def test_login5(self):  
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        user_name=driver.find_element_by_xpath("//input[@id='user-name']")
        password=driver.find_element_by_xpath("//input[@id='password']")
        login_button=driver.find_element_by_xpath("//input[@id='login-button']")

        user_name.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        error = driver.find_element_by_xpath("//span[contains(.,'Products')]")

        if(error.is_displayed()):
            print("Test2 ok")
        time.sleep(2) 

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()