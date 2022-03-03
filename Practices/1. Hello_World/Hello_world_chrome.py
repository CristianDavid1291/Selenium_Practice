from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/")

print(driver.title)

driver.close()