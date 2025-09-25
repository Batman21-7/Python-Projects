from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep

PROMISED_UP = 150
PROMISED_DOWN = 10
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = "pythontest217@gmail.com"
TWITTER_PASSWORD = "T0ny$t4rk21"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        sleep(5)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        sleep(40)

        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '8]/div/a').click()

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                       '2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/?lang=en")
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        sleep(5)

        input_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                       '2]/div/input')
        input_box.send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div/div/div/div[6]').click()
        sleep(1)

        input_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                       '3]/div/label/div/div[2]/div[1]/input')
        input_box.send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                           '2]/div[2]/div[2]/div/div[1]/div/div/div').click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
