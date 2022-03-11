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

def get_Data():
    return[

        ("rodrigo","1234"),
        ("juan","1234"),
        ("pedro","123asds4"),
        ("erika","1234"),
        ("Admin","admin123")
    ]

@pytest.mark.login
@pytest.mark.parametrize("user,password",get_Data())
def test1(user,password):
    global driver
    global f
    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    f = Function(driver)
    f.text_xpath_validate("//input[@id='txtUsername']",user,1,1)
    f.text_xpath_validate("//input[@id='txtPassword']",password,1,1)
    f.text_xpath_validate_click("//input[@id='btnLogin']",1,1)
    



def teardown_function():
    print("\nEnding Login2")
    driver.close()

