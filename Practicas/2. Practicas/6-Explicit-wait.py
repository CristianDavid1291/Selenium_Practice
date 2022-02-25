from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")

#Page Process
driver.get("https://demo.seleniumeasy.com/")

driver.maximize_window()
#driver.implicitly_wait(5)
t = 3

alertBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='at-cv-lightbox-button-holder']/a[2]")))
alertBtn.click()

driver.find_element_by_xpath("//a[text()='Input Forms']").click()
time.sleep(t)
driver.find_element_by_xpath("(//a[text()='Simple Form Demo'])[2]").click()
time.sleep(t)
driver.find_element_by_xpath("//input[@id='user-message']").send_keys("Hello World")






time.sleep(t)
#driver.close()