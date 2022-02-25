from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")

#Page Process
driver.get("https://demoqa.com/text-box")

driver.maximize_window()
driver.implicitly_wait(15) ## it waits and verifies while element charge
time.sleep(2)

name = driver.find_element_by_xpath("//input[contains(@id,'userName')]")
name.send_keys("Cristian")
driver.find_element_by_xpath("//input[contains(@id,'userEmail')]").send_keys("cristian@gmail.com")
driver.find_element_by_xpath("//textarea[contains(@id,'currentAddress')]").send_keys("This is a test current address 1")
driver.find_element_by_xpath("//textarea[contains(@id,'permanentAddress')]").send_keys("This is a test current address 2")
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_xpath("//button[contains(@id,'submit')]"))
driver.find_element_by_xpath("//button[contains(@id,'submit')]").click()

time.sleep(2)


driver.close()