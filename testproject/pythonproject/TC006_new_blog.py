# TC006 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random import randint
import time
import csv

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

# Load page
driver.get("http://localhost:1667/")
time.sleep(8)

try:
    url_title_list = []

    # Enter the data to be uploaded
    user_name = f"Rapid{randint(1, 99)}"
    user = [user_name, f"{user_name}@gmail.com", 'PassWord@123']


    # Driver find
    def find(xpath):
        elem = driver.find_element_by_xpath(xpath)
        return elem


    # Sign up
    def reg():
        find('//a[@href="#/register"]').click()
        time.sleep(5)
        find('//*[@placeholder="Username"]').send_keys(user[0])
        find('//*[@placeholder="Email"]').send_keys(user[1])
        find('//*[@placeholder="Password"]').send_keys(user[2])
        sign_up = find('//*[@id="app"]/div/div/div/div/form/button')
        sign_up.click()
        time.sleep(5)
        reg_ok = find('/html/body/div[2]/div/div[4]/div/button')
        reg_ok.click()


    reg()

    time.sleep(8)


    def creat_post():
        time.sleep(4)
        with open('C:\\Users\\User\\PycharmProjects\\conduit\\post.csv') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                find('//*[@href="#/editor"]').click()
                time.sleep(8)
                find('//*[@placeholder="Article Title"]').send_keys(row[0])
                find('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(row[1])
                find('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea').send_keys(row[2])
                find('//*[@placeholder="Enter tags"]').send_keys(row[3])
                find('//button[@type="submit"]').click()
                url_title_list.append(row[0].replace(" ", "-").lower())
                time.sleep(8)

            print(driver.find_element_by_tag_name("h1").text)
            assert driver.find_element_by_tag_name("h1").text == row[0]


    creat_post()


finally:
    driver.close()
