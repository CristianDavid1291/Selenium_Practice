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
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    f = Function(driver)
    f.text_xpath_validate("//input[@id='txtUsername']","Admin",1,1)
    f.text_xpath_validate("//input[@id='txtPassword']","admin123",1,1)
    f.text_xpath_validate_click("//input[@id='btnLogin']",1,1)

@pytest.mark.usefixtures("setup_l1")
@pytest.mark.t1
def test1():
    if(f.exist("xpath","//h1[contains(.,'Dashboard')]",2)):
        print("#######################################################\n")
        assert True
    else:
        assert False, "The object doesn't exist"    
 

def teardown_function():
    print("/nEnding Test")
    driver.close()


