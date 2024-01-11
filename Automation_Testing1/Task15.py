from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=25_28")
driver.find_element(By.XPATH,"//a[@id='compare-total']").click()
driver.implicitly_wait(5)
msg = driver.find_element(By.XPATH,"//*[@id='content']/h1").text
msg2 = driver.find_element(By.XPATH,"//p[normalize-space()='You have not chosen any products to compare.']").text

print(msg)
print(msg2)
driver.find_element(By.XPATH,"//a[@class='btn btn-light']").click()