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

try:
    # Oldal betöltése
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Feltöltendő adatok megadása
    email = 'username5005@gmail.com'
    pwd = 'Username5005'

    # Post mezők xpath
    title = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'


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


    # Write post
    def write_post():
        find('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        time.sleep(2)
        with open('../text/post.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                find(title).send_keys(row[0])
                find(about).send_keys(row[1])
                find(write).send_keys(row[2])
                find(tags).send_keys(row[3])
        write_btn = find('//*[@id="app"]/div/div/div/div/form/button')
        write_btn.click()


    write_post()
    print(write_post)
    time.sleep(2)


    # Controll
    def controll():
        with open('../text/post.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                assert (row[0] in find('//*[@id="app"]/div/div[1]/div/h1').text)
                assert (row[2] in find('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text)
                assert (row[3] in find('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/a').text)


    controll()



finally:
    driver.close()
