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
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
driver.implicitly_wait(5)
links = driver.find_elements(By.XPATH,"(//div[@class='col-sm-3'])//a")

for link in links:
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

time.sleep(3)
driver.quit()