# TC005 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import string
import random

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

# Load page
driver.get("http://localhost:1667/")
time.sleep(3)

# Enter the data to be uploaded
email = 'testuser1@example.com'
username = 'testuser1'
pwd = 'Abcd123$'

# Post fields xpath
title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
write_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
tags_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'

# Button xpath
sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_inbtn = '//*[@id="app"]/div/div/div/div/form/button'
new_artbtn = '//*[@id="app"]/nav/div/ul/li[2]/a'
publish = '//*[@id="app"]/div/div/div/div/form/button'


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Sign in
def sign_in(email, pwd):
    sign_button = find(sign_btn)
    sign_button.click()
    find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
    find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(pwd)
    sign_in_btn = find(sign_inbtn)
    sign_in_btn.click()
    time.sleep(2)


sign_in(email, pwd)
time.sleep(3)

assert username == find('//*[@id="app"]/nav/div/ul/li[4]/a').text
print(username)
time.sleep(2)


# Determining the number of original posts
def control():
    find('//*[@id="app"]/nav/div/ul/li[4]/a').click()  # username click
    find('//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a').click()  # my article click
    post_number_list = driver.find_elements_by_class_name('article-preview')  # my article's number list
    print(len(post_number_list))  # my article's number
    post_number = len(post_number_list)
    print(post_number)


control()

try:
    # Write new post
    def new_post():
        find(new_artbtn).click()
        with open('post.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                find(title_x).send_keys(row[0])
                find(about_x).send_keys(row[1])
                find(write_x).send_keys(row[2])
                find(tags_x).send_keys(row[3])
                find(publish).click()


    new_post()

    time.sleep(2)


    # Check
    def check():
        find('//*[@id="app"]/nav/div/ul/li[4]/a').click()   # username click
        find('//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a').click()     # my article click
        new_post_number_list = driver.find_elements_by_class_name('article-preview')    # my article's new number list
        print(len(new_post_number_list))
        new_post_number = len(new_post_number_list)
        print(new_post_number)


    check()

    assert (post_number + 1) == new_post_number
    print(post_number + 1)

finally:
    driver.close()
