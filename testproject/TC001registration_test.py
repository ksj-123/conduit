# TC001_test - User Registration (random data) (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import string

options = Options()
options.headless = True


class TestUserReg(object):
    def test_registration(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # Load page
        self.driver.get("http://localhost:1667/")
        time.sleep(8)

        # Fields xpath
        sign_up_btn = '//*[@id="app"]/nav/div/ul/li[3]/a'
        username_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
        email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
        pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input'
        sign_up_x = '//*[@id="app"]/div/div/div/div/form/button'

        # Enter the data to be uploaded
        email = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10)) + '@mail.com'
        pwd = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10)) + '@1234'
        username = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(10)))

        # Sign up
        self.driver.find_element(By.XPATH, sign_up_btn).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, username_x).send_keys(username)
        self.driver.find_element(By.XPATH, email_x).send_keys(email)
        self.driver.find_element(By.XPATH, pwd_x).send_keys(pwd)
        with open("C:\\Users\\User\\PycharmProjects\\conduit\\reg_data2.csv", mode="w") as file:
            file.write(username + "," + email + "," + pwd)
        self.driver.find_element(By.XPATH, sign_up_x).click()
        time.sleep(15)

        # Check box
        assert ('Welcome!' in self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]').text)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div/button").click()

        self.driver.close()
        self.driver.quit()
