from selenium import webdriver




driver = webdriver.Ie("Drivers\Explorer\IEDriverServer.exe")

driver.get("https://admin-demo.nopcommerce.com/login")
driver.execute_script(script="document.getElementById('Email').value='admin@yourstore.com'")
driver.execute_script(script="document.getElementById('Password').value='admin'")
driver.execute_script(script="document.getElementsByClassName('button-1 login-button')[0].click()")



# f.text_xpath_validate("//input[@id='contenido-form:usuario']","admin@yourstore.com",1,1)
# f.text_xpath_validate("//input[@id='contenido-form:clave']","admin",1,1)
