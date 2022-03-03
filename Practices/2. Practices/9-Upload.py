from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome(executable_path=".\Drivers\Chrome\chromedriver.exe")
t = 3
#driver = webdriver.Firefox(executable_path=".\Drivers\Firefox\geckodriver.exe")

#Page Process
driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.implicitly_wait(10)

try:
    findFileBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[contains(@type,'file') and contains(@id,'fileinput')]")))
    findFileBtn = driver.find_element_by_xpath("//input[contains(@type,'file') and contains(@id,'fileinput')]")
    findFileBtn.send_keys("F:\CRISTIAN\Cursos\Selenium\Practices\img\child.jpg")
    driver.find_element_by_xpath("//label[@for='itsanimage']").click()
    driver.find_element_by_xpath("//input[@type='submit' and @name='upload']").click()
    
except TimeoutException as ex:
    print (ex.msg)



time.sleep(3)
driver.close()