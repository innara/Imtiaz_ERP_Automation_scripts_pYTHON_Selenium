from telnetlib import EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("some URL")
driver.set_page_load_timeout(20)
email = driver.find_element(By.NAME, "email")
email.send_keys("emal example")
password = driver.find_element(By.NAME, "password")
password.send_keys("password")
time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="formAuthentication"]/button')
login.submit()
if "dashboard" in driver.current_url:
    print("Login successful Your credentials are correct!")
else:
    print("Login failed. Please check your credentials.")
time.sleep(5)

# Accessing Broker from Side bar
driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[7]/a').click()
time.sleep(2)

driver.quit()