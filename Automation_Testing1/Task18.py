from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")
img_elem = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/form/div/div[1]/a/img")
img_src = img_elem.get_attribute('src')
print(f"Image Src: {img_src}")

# Close the browser
driver.quit()