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


@pytest.fixture(scope='module')
def setup_l1():
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
    yield
    print("\nEnding Login1")
    driver.close()

@pytest.fixture(scope='module')
def setup_l2():
    global driver
    global f
    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    f = Function(driver)
    f.text_xpath_validate("//input[@id='txtUsername']","Admin",1,1)
    f.text_xpath_validate("//input[@id='txtPassword']","admin123",1,1)
    f.text_xpath_validate_click("//input[@id='btnLogin']",1,1)
    yield
    print("/nEnding Login2")
    driver.close()

@pytest.mark.usefixtures("setup_l1")
def test1():
    print("Starting l1")
    f.text_xpath_validate_click("(//p[contains(.,'Customers')])[1]",.5,.5)
    f.text_xpath_validate_click("//a[@href='/Admin/Customer/List'][contains(.,'Customers')]",.5,.5)
    f.text_xpath_validate("//input[@id='SearchFirstName']","victoria",1,.5)
    f.text_xpath_validate_click("//button[@id='search-customers']",1,.5)
    f.text_xpath_validate_click("//a[@href='/Admin/Customer/Create']",1,.5)
    f.text_xpath_validate("//input[contains(@id,'Email')]","victoria@gmail.com",1,.5)
    f.text_xpath_validate("//input[contains(@id,'Password')]","123456",1,.5)
    f.text_xpath_validate("//input[@id='FirstName']","Victoria",1,.5)
    f.text_xpath_validate("//input[@id='LastName']","Aida",1,2)


# @pytest.mark.usefixtures("setup_l2")
# def test2():
#     print("Starting l2")