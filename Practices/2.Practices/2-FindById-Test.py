from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

name = driver.find_element_by_id("userName")
name.send_keys("Cristian")
driver.find_element_by_id("userEmail").send_keys("cristian@gmail.com")
driver.find_element_by_id("currentAddress").send_keys("This is a test current address 1")
driver.find_element_by_id("permanentAddress").send_keys("This is a test current address 2")
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_id("submit"))
driver.find_element_by_id("submit").click()

time.sleep(2)


driver.close()