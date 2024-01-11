from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver  = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")

# printing web element as text
msg1 = driver.find_element(By.XPATH,"//div[@id='narbar-menu']").text
print(msg1)
print("#######################################################")
msg2 = driver.find_element(By.XPATH,"//*[@id='top']").text
print(msg2)

driver.maximize_window()