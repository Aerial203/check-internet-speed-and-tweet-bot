from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL = input("Enter your twitter email/username: ")
PASSWORD = input("Enter your password: ")
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        test_speed_endpoint = "https://www.speedtest.net/"
        self.driver.get(url=test_speed_endpoint)
        time.sleep(10)
        go_field = self.driver.find_element_by_css_selector(".start-button a")
        go_field.click()
        time.sleep(20)
        result_download_field = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/'
            'div[2]/div/div[2]/span'
        )
        time.sleep(10)
        result_upload_field = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
            '/div[3]/div/div[2]/span'
        )
        self.down = result_download_field.text
        self.up = result_upload_field.text
        print(f"download speed: {self.down}")
        print(f"upload speed: {self.up}")
        # self.driver.quit()

    def tweet_at_provider(self):
        twitter_end_point = "https://twitter.com"
        self.driver.get(url=twitter_end_point)
        time.sleep(20)
        login_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]'
        )
        login_field.click()
        time.sleep(10)
        email_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
        )
        email_field.send_keys(EMAIL)
        password_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
        )
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(20)
        tweet_msg = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up " \
                    f"When I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        tweet_text_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/'
            'div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/span'
        )
        tweet_text_field.send_keys(tweet_msg)
        tweet_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/'
            'div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div'
        )
        tweet_field.click()
        time.sleep(10)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
bot.tweet_at_provider()
