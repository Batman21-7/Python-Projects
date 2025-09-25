from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3872077588&f_LF=f_AL&geoId=102257491&keywords=python"
               "%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(1)

username = driver.find_element(By.ID, "username")
username.send_keys("pythontest217@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("T0ny$t4rk21")
sign_in_button = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
sign_in_button.click()
time.sleep(3)

block = driver.find_element(By.ID, "ember43")
block.click()
save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save.click()
# follow = driver.find_element(By.CLASS_NAME, "follow")
# follow.click()
