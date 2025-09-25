from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

input_box = driver.find_element(By.NAME, "fName")
input_box.send_keys("Bruce")
input_box = driver.find_element(By.NAME, "lName")
input_box.send_keys("Wayne")
input_box = driver.find_element(By.NAME, "email")
input_box.send_keys("Bruce@WayneEnterprise.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()
