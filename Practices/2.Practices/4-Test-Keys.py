from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")


#Page Process
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
name = driver.find_element_by_id("userName")
name.send_keys("Cristian")
name.send_keys(Keys.TAB + "cristian@gmail.com" + Keys.TAB + "Adress1" + Keys.TAB + "adress2" + Keys.TAB + Keys.ENTER)
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_id("submit"))
time.sleep(2)
driver.close()

