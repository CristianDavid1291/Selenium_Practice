from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")

#Page Process
driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t = 2

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//label[contains(.,'Option 1')]")))
btn1.click()

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//label[contains(.,'Option 2')]")))
btn1.click()

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//label[contains(.,'Option 3')]")))
btn1.click()

time.sleep(t)

driver.close()