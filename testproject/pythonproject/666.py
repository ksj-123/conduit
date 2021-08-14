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

# User xpath
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'

# Post fields xpath
title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
write_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
tags_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
post_x = '//*[@class="article-preview"]'

# Button xpath
sign_up_btn = '//*[@id="app"]/nav/div/ul/li[3]/a'
sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_inbtn = '//*[@id="app"]/div/div/div/div/form/button'
new_artbtn = '//*[@id="app"]/nav/div/ul/li[2]/a'
publish = '//*[@id="app"]/div/div/div/div/form/button'
home_btn = '//*[@id="app"]/nav/div/ul/li[1]/a'
sign_up_x = '//*[@id="app"]/div/div/div/div/form/button'
o_btn = '/html/body/div[2]/div/div[4]/div'

# Enter the data to be uploaded
user_name = f"Rapid{randint(1, 99)}"
user = [user_name, f"{user_name}@gmail.com", 'PassWord@123']


# Driver find
def find(xpath):
    elem = driver.find_element_by_xpath(xpath)
    return elem

    # Sign up


def reg():
    find(sign_up_btn).click()
    time.sleep(5)
    find(username_x).send_keys(user[0])
    find(email_x).send_keys(user[1])
    find(pwd_x).send_keys(user[2])
    sign_up = find(sign_up_x)
    sign_up.click()
    time.sleep(5)
    reg_ok = find(o_btn)
    reg_ok.click()

    reg()


time.sleep(5)

assert user_name == find(username_x).text
# print(username)
time.sleep(2)

try:
    url_title_list = []


    def creat_post():
        time.sleep(4)
        with open('C:\\Users\\User\\PycharmProjects\\conduit\\post.csv') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                find(new_artbtn).click()
                time.sleep(3)
                find(title_x).send_keys(row[0])
                find(about_x).send_keys(row[1])
                find(write_x).send_keys(row[2])
                find(tags_x).send_keys(row[3])
                find(publish).click()
                url_title_list.append(row[0].replace(" ", "-").lower())
                time.sleep(3)


    creat_post()

    # Check URL
    time.sleep(3)
    username_link = find(username_x)
    username_link.click()
    time.sleep(3)

    # Attributes of the created blogs
    # (from index 5 because there is another one created for 'testuser1')
    blogs_href = driver.find_elements_by_xpath('//div//a[@class="preview-link"]')
    urls = []
    for b in blogs_href:
        # print(_.get_attribute("href"))
        urls.append(b.get_attribute("href"))
    print(urls)

    # Check URL
    for i, j in zip(url_title_list, urls):
        assert f'http://localhost:1667/#/articles/{i}' == driver.current_url

        # print(f'http://localhost:1667/#/articles/{i}')
        # print(j)


finally:
    driver.close()
