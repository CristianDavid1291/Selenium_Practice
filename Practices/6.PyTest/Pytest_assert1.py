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


@pytest.mark.validateIf
def test_validate_if():
    name1 = "Cristian"
    name2 = "David"

    assert name1 == name2, "The name are differents"

@pytest.mark.validateNum
def test_validate_nums():
    num1 = 21
    num2 = 20

    assert num1 < num2, "Num1 > Num 2"

@pytest.mark.contentValidation
def test_validate():
    date = "Cristian"
    date2 = "it is a complete sentence"

    assert date in date2, "The date isn't in date2"

@pytest.mark.doubleValidation
def test_doubleValidation():
    a = 20
    b = 40

    if (a == b):
        print ("\n The dates are the same")
        assert True
    else:
        assert False, "The Data is different"   
