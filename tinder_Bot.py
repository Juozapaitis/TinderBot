from selenium import webdriver
from tkinter import messagebox
from time import sleep
from secrets import your_number
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://tinder.com')
        delay = 0.01
        try:
            element = WebDriverWait(driver, delay).until(EC.presence_of_element_titleIs(("TINDER | Rask simpatijų. Bendrauk. Eik į pasimatymą")))
        except Exception:
            print("No")
            
        nr_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[3]/button')
        nr_button.click()

        sleep(random.uniform(2, 3))

        number_in = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div/input')
        number_in.send_keys(your_number)

        sleep(random.uniform(2, 3))

        continue_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button')
        continue_button.click()

        messagebox.showinfo(title='verification', message='Finish on screen verification, and then click OK.')

        sleep(1.5)

        continue_button_verification = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/button[2]')
        continue_button_verification.click()

        sleep(5)

        getLocation = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        getLocation.click()

        sleep(2.3)

        no_messages = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        no_messages.click()

    def like(self):
        like_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    def dislike(self):
        dislike_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_button.click()

    def auto_swipe(self):
        while True:
            delay = 3
            sleep(random.uniform(0.5, 2))
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        try:
                            self.no_likes()
                        except:
                            break

        
    def close_popup(self):
        popup_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
        popup_1.click()
    
    def close_match(self):
        match_close = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/a')
        match_close.click()

    def no_likes(self):
        no_likes_close = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]')
        no_likes_close.click()


bot = TinderBot()
bot.login()
bot.auto_swipe


        


