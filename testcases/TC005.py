# TC005 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv

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
sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_inbtn = '//*[@id="app"]/div/div/div/div/form/button'
new_artbtn = '//*[@id="app"]/nav/div/ul/li[2]/a'
publish = '//*[@id="app"]/div/div/div/div/form/button'
home_btn = '//*[@id="app"]/nav/div/ul/li[1]/a'


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Sign in
def sign_in(email, pwd):
    sign_button = find(sign_btn)
    sign_button.click()
    find(email_x).send_keys(email)
    find(pwd_x).send_keys(pwd)
    sign_in_btn = find(sign_inbtn)
    sign_in_btn.click()
    time.sleep(2)


sign_in(email, pwd)
time.sleep(3)

assert username == find(username_x).text
print(username)
time.sleep(2)

try:
    def creat_post(row):
        find(new_artbtn).click()
        print(row)
        find(title_x).send_keys(row[0])
        find(about_x).send_keys(row[1])
        find(write_x).send_keys(row[2])
        find(tags_x).send_keys(row[3])
        find(publish).click()
        driver.back()


    # for _url_title_list:

    # def check_post(row):
    #     find(home_btn).click()  # Home button click
    #     title = find(post_x).send_keys(row[0])
    #     expect_url 'http://localhost:1667/#/articles/{title.lower }'
    #     print(row[0])
    #     driver.back()
    #     # title = driver.find_element_by_link_text(row[''][0])  # Find new blog link
    #     # print(title)
    #     url_title = row[0]
    #
    # #     # 'http://localhost:1667/#/articles/ez-egy-uj-blog'
    #
    #     lines = csv.readlines()

    # Write new post
    def new_post():
        with open('../text/post.csv') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                creat_post(row)
                url_title_list = []
                url_title_list.append(row[0].replace(" ", "-"))


    time.sleep(2)
    new_post()
    print(url_title_list)

    # for i in url_title_list:
    #     assert 'http://localhost:1667/#/articles/{_}' == driver.current_url()
    #     print('http://localhost:1667/#/articles/{_}')
    #     print(driver.current_url())

finally:
    pass
#     driver.close()
