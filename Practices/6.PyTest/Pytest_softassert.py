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


@pytest.mark.run
def test_one():
    print("First test")
    assert True

@pytest.mark.run
def test_two():
    a = 10
    b = 10
    assert a == b, "The numbers are different"
    assert a != b, "They are the same"
    assert a > b, "A is greater than B"
    assert a < b, "A is smaller than B"

@pytest.mark.run
def test_three():
    a = 15
    b = 20
    assert a > b, "The number A isn't grater than B"

@pytest.mark.run
def test_four():
    name = "Cristian"
    assert name == "Cris", "The name isn't Cristian"

