import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located

TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
PROMISED_DOWN = 150
PROMISED_UP = 10




class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome()


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        go_button.click()
        sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        print(f" down : {self.down}")
        print(f" up : {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")

        #Log in to twitter
        email_box = self.driver.find_element(By.CLASS_NAME, "css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3")
        email_box.send_keys(TWITTER_EMAIL)
        click_next = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]")
        click_next.click()
        my_password = self.driver.find_element(By.NAME, "password")
        my_password.send_keys(TWITTER_PASSWORD)
        my_password.send_keys(Keys.ENTER)
        sleep(10)

        #Post twitter about your internet speed
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            send_tweet = self.driver.find_element(By.ID, "placeholder-3rbh9")
            send_tweet.send_keys(f"Hey internet Provider, why is my internet speed"
                                 f"{self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up ")
            post_tweet = self.driver.find_element(By.CLASS_NAME, "css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3")
            post_tweet.click()
            sleep(10)

        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()


