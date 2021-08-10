# TC001 - User Registration (random data)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
import string

opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)


def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Fields xpath
sign_up_btn = '//*[@id="app"]/nav/div/ul/li[3]/a'
username_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input'
sign_up_x = '//*[@id="app"]/div/div/div/div/form/button'

# Enter the data to be uploaded
email = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10)) + '@mail.com'
pwd = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(10)))
username = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(10)))

try:
    # Load page
    URL = driver.get("http://localhost:1667/")
    time.sleep(2)


    # Sign up
    def reg():
        find(sign_up_btn).click()
        time.sleep(2)
        find(username_x).send_keys(username)
        find(email_x).send_keys(email)
        find(pwd_x).send_keys(pwd)
        sign_up = find(sign_up_x)
        sign_up.click()


    reg()
    print(reg)
    time.sleep(5)

    # Check box
    assert ('Welcome!' in find('/html/body/div[2]/div/div[2]').text)
    time.sleep(5)
    find("/html/body/div[2]/div/div[4]/div/button").click()
    time.sleep(5)

finally:
    driver.close()
