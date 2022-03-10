import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Excel_Functions.Functions import Function
from Excel_Functions.Page_Logins import Page_Login
driver=""
f=""

def setup_function(function):
    global driver
    global f
    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.maximize_window()
    f = Function(driver)
    f.text_xpath_validate("//input[@id='Email']","admin@yourstore.com",1,1)
    f.text_xpath_validate("//input[@id='Password']","admin",1,1)
    f.text_xpath_validate_click("//input[@id='RememberMe']",1,1)
    f.text_xpath_validate_click("//button[contains(.,'Log in')]",1,1)

# def test1():
#     f.text_xpath_validate_click("(//p[contains(.,'Catalog')])[1]",1,1)
#     f.text_xpath_validate_click("//a[@href='/Admin/Product/List'][contains(.,'Products')]",1,1)
#     f.text_xpath_validate("//input[@id='SearchProductName']","Computer",1,1)
#     f.text_xpath_validate_click("//button[@id='search-products']",1,1)

def test2():
    f.text_xpath_validate_click("(//p[contains(.,'Catalog')])[1]",1,1)
    f.text_xpath_validate_click("//a[@href='/Admin/Product/List'][contains(.,'Products')]",1,1)
    f.text_xpath_validate_click("//a[contains(.,'Add new')]",1,1)
    f.text_xpath_validate("//input[@id='Name']","Laptop Dell",1,1)
    f.text_xpath_validate("//textarea[contains(@id,'ShortDescription')]","Laptop Dell Short description",1,1)
    f.text_xpath_validate_click("//span[contains(.,'File')]",1,1)
    f.text_xpath_validate_click("//div[@class='tox-collection__item-label'][contains(.,'New document')]",1,1)
    driver.switch_to.frame(0)
    f.text_xpath_validate("//body[@id='tinymce']","Iframe Test",1,1)
    driver.switch_to.default_content()
    f.text_xpath_validate("//input[contains(@id,'Sku')]","SKU:123546",1,1)
    time.sleep(2)

    





    


def teardown_function(function):
    print("\nEnding test")
    driver.close()