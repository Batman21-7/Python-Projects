from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

FORM_LINK = ("https://docs.google.com/forms/d/e/1FAIpQLSdNe4YPI12b_sUmEzviJEwbccHW606310BC-xfp3PG8lIYWKA/viewform?usp"
             "=sf_link")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


def fill_form(address, href, price):
    driver.get(url=FORM_LINK)
    input_div = driver.find_element(By.CLASS_NAME, 'o3Dpx')
    inputs = input_div.find_elements(By.TAG_NAME, 'input')
    inputs[0].send_keys(address)
    inputs[1].send_keys(price)
    inputs[2].send_keys(href)
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()  # Submit button click


webpage = requests.get(url="https://appbrewery.github.io/Zillow-Clone/").text
soup = BeautifulSoup(webpage, 'html.parser')

houses = soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
for house in houses:
    # house = houses[0]
    address = house.find(name='a').getText().strip().replace(' |', ',')
    price = house.find(name='span', class_="PropertyCardWrapper__StyledPriceLine").getText()
    price = price.split('+')[0].split('/')[0]
    href = house.find(name='a').get('href')
    # print(f"address: {address}, href:{href}, price: {price}")
    fill_form(address, href, price)

driver.get(url=f"https://docs.google.com/forms/d/1xvKnPfzE1VRO6WsgrtEqc_w4VfxGf4c4zzW4Y4isj5k/edit#responses")
sleep(1)
driver.find_element(By.XPATH, '//*[@id="inproduct-guide-modal"]/div[3]/button').click()
sleep(1)
# driver.find_element(By.LINK_TEXT, "Sign in").click()
# driver.find_element(By.ID, "identifierId").send_keys("pythontest217")
driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div').click()

# sleep(5)
# driver.quit()
