from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python\n")

# driver.quit()
