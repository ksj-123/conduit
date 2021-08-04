# TC008 - My blog post delete
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

try:
    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Enter the data to be uploaded
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'

    # Post fields xpath
    title_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'


    # Driver find
    def find(xpath):
        find = driver.find_element_by_xpath(xpath)
        return find


    # Sign in
    def sign_in(email, pwd):
        sign_button = find('//*[@id="app"]/nav/div/ul/li[2]/a')
        sign_button.click()
        find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
        find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(pwd)
        sign_in_btn = find('//*[@id="app"]/div/div/div/div/form/button')
        sign_in_btn.click()
        time.sleep(2)


    sign_in(email, pwd)
    time.sleep(3)

    # Post delete
    def delete():
        find('//*[@id="app"]/nav/div/ul/li[4]/a').click()  # username click
        time.sleep(2)
        find('//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a').click()  # my title click
        time.sleep(2)
        find('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1').click()  # post title click
        time.sleep(2)
        find('//*[@id="app"]/div/div[1]/div/div/span/button/span').click()  # delete button click
        time.sleep(2)


    delete()
    print(delete)
    time.sleep(2)


    # Control
    # assert


finally:
    driver.close()
