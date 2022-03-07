from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Functions.Functions import Functions

class Login_Page():

    def __init__(self,driver):
        self.driver = driver

    def main_process_login_page(self):
        driver = self.driver
        f = Functions(driver)
        f.navigate("https://www.saucedemo.com/")
        f.time(1)
        f.text_xpath_validate("//input[@id='user-name']","Cristian",2,1)
        f.text_xpath_validate("//input[@id='password']","1234",2,1)
        f.text_xpath_validate_click("//input[@id='login-button']",2,1)
        