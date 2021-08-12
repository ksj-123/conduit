# TC007 - Edit blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

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

# Fields xpath
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
sign_button_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
my_title_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
post_tilte_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1'
title_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
about_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
write_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
tags_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
edit_xp = '//*[@id="app"]/div/div[1]/div/div/span/a'
tags_btn_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]'
publish_btn_x = '//*[@id="app"]/div/div/div/div/form/button'

# Test data
title_2 = 'Blog mod'
about_2 = 'Blog'
write_2 = 'Ez nem mese'
tags_2 = 'Rémálom'


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


try:

    # Sign in
    def sign_in(email, pwd):
        sign_button = find(sign_button_x)
        sign_button.click()
        find(email_x).send_keys(email)
        find(pwd_x).send_keys(pwd)
        sign_in_btn = find(sign_in_btn_x)
        sign_in_btn.click()
        time.sleep(2)


    sign_in(email, pwd)
    time.sleep(2)

    # Find one of my post
    find('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(2)


    # Post modification
    def edit():
        find(username_x).click()  # username click
        time.sleep(2)
        find(my_title_x).click()  # my title click
        time.sleep(2)
        find(post_tilte_x).click()  # post title click
        time.sleep(2)
        find(edit_xp).click()  # edit article button click
        time.sleep(2)
        find(title_xp).clear()
        find(title_xp).send_keys(title_2)
        find(about_xp).clear()
        find(about_xp).send_keys(about_2)
        find(write_xp).clear()
        find(write_xp).send_keys(write_2)
        tags_btn = find(tags_btn_x)
        tags_btn.click()
        find(tags_xp).send_keys(tags_2)
        publish_btn = find(publish_btn_x)
        publish_btn.click()


    edit()

    time.sleep(2)

    # Controll
    assert (title_2 in find('//*[@id="app"]/div/div[1]/div/h1').text)
    assert (write_2 in find('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text)
    assert (tags_2 in find('//*[@id="app"]/div/div[2]/div[1]/div/div[2]').text)
    print(title_2, write_2, tags_2)



finally:
    driver.close()
