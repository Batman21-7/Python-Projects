from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

dictionary = {}

text = driver.find_element(By.CSS_SELECTOR, ".event-widget div ul").text.split('\n')

for i in range(0, 10, 2):
    dictionary[i//2] = {"time": text[i], "name": text[i+1]}
print(dictionary)

driver.quit()
