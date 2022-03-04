from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")
t=3
#Page Process
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
driver.find_element_by_xpath("//a[@href='#myModal0']").click()


try:
    alertBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"(//a[contains(.,'Save changes')])[1]")))
    alertBtn.click()
except TimeoutException as ex:
    print(ex)
    print("Element not found")

time.sleep(3)
driver.close()