from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Excel_Functions.Functions import Function

class Page_Login():
  
  def __init__(self) -> None:
      pass
   
  def l1(self,email,password,xpathValidation):
    driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    f = Function(driver)
    f.navigate("https://admin-demo.nopcommerce.com/login")
    time.sleep(2)
    f.text_xpath_validate("//input[@id='Email']",email,1,1)
    f.text_xpath_validate("//input[@id='Password']",password,1,1)
    f.text_xpath_validate_click("//input[@id='RememberMe']",1,1)
    f.text_xpath_validate_click("//button[contains(.,'Log in')]",1,1)
    
    if(f.exist("xpath",xpathValidation,1)):
        print("-----------Test validation wrong account succesful")
    else:
        print("------------Test validation wrong account error")  
    driver.close()

    