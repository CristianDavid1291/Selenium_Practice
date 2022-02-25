from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")

driver.get("https://demo.seleniumeasy.com/")

print(driver.title)

driver.close()