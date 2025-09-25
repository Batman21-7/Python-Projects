from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
time.sleep(2)

login = driver.find_element(By.LINK_TEXT, "Log in")
login.click()
time.sleep(1)
facebook_button = driver.find_element(By.XPATH, '//*[@id="t-1302454380"]/main/div[1]/div/div[1]/div/div/div[2]'
                                                '/div[2]/span/div[2]/button')
facebook_button.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

driver.find_element(By.ID, "email").send_keys("pythontest217@gmail.com")
driver.find_element(By.ID, "pass").send_keys("T0ny$t4rk21")
driver.find_element(By.ID, "loginbutton").click()
time.sleep(6)

driver.switch_to.window(base_window)

driver.find_element(By.XPATH, '//*[@id="t-1302454380"]/main/div[2]/div/div/div[1]/div[2]/button').click()
driver.find_element(By.XPATH, '//*[@id="t-1302454380"]/main/div[1]/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, '//*[@id="t-1302454380"]/main/div/div/div/div[3]/button[2]').click()
time.sleep(10)

no_button = driver.find_element(By.XPATH,'')

for i in range(5):
    no_button.click()
    time.sleep(1)
