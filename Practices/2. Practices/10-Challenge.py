from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

t = 3
driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
driver.maximize_window()
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")

#Page Process
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.implicitly_wait(10)

driver.find_element_by_xpath("//input[@name='first_name' and @type='text']").send_keys("Cristian")
driver.find_element_by_xpath("//input[@name='last_name' and @type='text']").send_keys("David")
driver.find_element_by_xpath("//input[@name='email' and @type='text']").send_keys("cristiandavid@gmail.com")
driver.find_element_by_xpath("//input[@name='phone' and @type='text']").send_keys("(845)2222222")
driver.find_element_by_xpath("//input[@name='address' and @type='text']").send_keys("Cra 21-77")
driver.find_element_by_xpath("//input[@name='city' and @type='text']").send_keys("Manizales")
driver.find_element_by_xpath("//input[@name='city' and @type='text']").send_keys("Manizales")
sd = Select(driver.find_element_by_xpath("//select[@name='state']"))
sd.select_by_index(4)
driver.find_element_by_xpath("//input[@name='zip']").send_keys("1700")
driver.find_element_by_xpath("//input[@name='website']").send_keys("www.prueba.com")
driver.find_element_by_xpath("//input[@type='radio' and @value='yes']").click()
driver.find_element_by_xpath("//textarea[@name='comment']").send_keys("Testing text area")
# driver.find_element_by_xpath("//button[contains(.,'Send ') and @type='submit']").click()


try:
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Send ') and @type='submit']")))
    btn.click()
    print("Click")
except TimeoutException as ex:
    print(ex)
    print("Incorrect data")

time.sleep(t)
driver.close()