from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
t = 2
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")

#Page Process
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.implicitly_wait(10)



try:
    selectDays = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//select[@id='select-demo']")))
    sd = Select(selectDays)
    sd.select_by_visible_text("Sunday")
    time.sleep(t)

    sd.select_by_index(2)
    time.sleep(t)
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_xpath("//select[contains(@id,'multi-select') and contains(@name,'States')]"))
except TimeoutException as ex:
    print(ex.msg)
    print ("Elemento no disponible")
    

states = Select(driver.find_element_by_xpath("//select[contains(@id,'multi-select') and contains(@name,'States')]"))
states.select_by_index(1)
states.select_by_index(2)
states.select_by_index(5)

time.sleep(3)

driver.close()