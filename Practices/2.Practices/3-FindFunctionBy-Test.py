from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")


#Page Process
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
name = driver.find_element(By.ID,"userName")
name.send_keys("Cristian")
driver.find_element(By.ID,"userEmail").send_keys("cristian@gmail.com")
driver.find_element(By.ID,"currentAddress").send_keys("This is a test current address 1")
driver.find_element(By.ID,"permanentAddress").send_keys("This is a test current address 2")
driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID,"submit"))
driver.find_element(By.ID,"submit").click()
time.sleep(2)
driver.close()