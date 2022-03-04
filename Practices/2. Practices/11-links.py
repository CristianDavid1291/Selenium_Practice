from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
t = 2

#Page Process
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

#all links from page
links = driver.find_elements(By.TAG_NAME,"a")
print (len(links))

# for num in links:
#     print(num.text)

driver.find_element_by_link_text("Date pickers").click()
driver.find_element_by_link_text("JQuery Date Picker").click()

time.sleep(t)
driver.close()