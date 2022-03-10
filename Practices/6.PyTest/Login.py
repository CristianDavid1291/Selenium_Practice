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



def test_login1():
    
    fl = Page_Login()
    fl.l1("cristian@gmail.com","123456","//li[contains(.,'No customer account found')]")
    fl.l1("","123456","//span[@id='Email-error' and contains(.,'Please enter your email')]")
    fl.l1("cristian","Cristian","//span[@id='Email-error' and contains(.,'Wrong email')]")
    fl.l1("admin@yourstore.com","admin","//h1[contains(.,'Dashboard')]")

    


