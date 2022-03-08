from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
t=3
bandera = False
#Page Process
driver.get("https://demoqa.com/")
driver.maximize_window()

try:
    titleImage =driver.find_element_by_xpath("//img[@src='/images/Tooqa.jpg']")
    bandera=titleImage.is_displayed()
except TimeoutException as ex:
    print(ex)


if(bandera):
    driver.find_element_by_xpath("//div[@class='card-body' and contains(.,'Elements')]").click()
else:
    print("Page not found")

time.sleep(t)
driver.close()