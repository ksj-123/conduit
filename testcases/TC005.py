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

try:
    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Enter the data to be uploaded
    email = 'username5555@gmail.com'
    username = 'username5555'
    pwd = 'Username5555'


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

    # Controll
    assert # az új poszt címét, stb.-t kellene összehasonlítani a felület és a post.csv tartalma között???

finally:
    driver.close()
