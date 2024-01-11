import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")
driver.maximize_window()
action = ActionChains(driver)
element = driver.find_element(By.XPATH,"//a[normalize-space()='Laptops & Notebooks']")
action.context_click(element).send_keys(Keys.ARROW_DOWN).pause(2)\
    .send_keys(Keys.ENTER).pause(2).perform()

driver.implicitly_wait(3)