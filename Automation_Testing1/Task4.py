from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")
driver.find_element(By.XPATH,"//*[@id='search']/input").send_keys("Computer")
driver.find_element(By.XPATH,"//button[@class='btn btn-light btn-lg']").click()
driver.maximize_window()