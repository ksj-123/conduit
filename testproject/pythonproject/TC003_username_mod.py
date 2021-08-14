# TC004 - User data modification
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random import randint
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)

# Load page
driver.get('http://localhost:1667/')
time.sleep(2)


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Fields xpath
sign_up_btn = '//*[@id="app"]/nav/div/ul/li[3]/a'
username_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input'
sign_up_x = '//*[@id="app"]/div/div/div/div/form/button'
o_btn = '/html/body/div[2]/div/div[4]/div'

# Enter the data to be uploaded
user_name = f"Rapid{randint(1, 99)}"
user = [user_name, f"{user_name}@gmail.com", 'PassWord@123']
new_username = 'remek'

try:
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

    # Settings - username modification
    def mod():
        settings = find('//*[@href="#/settings"]')
        settings.click()
        time.sleep(2)
        username = find('//*[@placeholder="Your username"]')
        username.clear()
        username.send_keys(new_username)
        update = find('//*[@id="app"]/div/div/div/div/form/fieldset/button')
        update.click()
        time.sleep(5)
        ok_btn = find('/html/body/div[2]/div/div[3]/div/button')
        ok_btn.click()
        time.sleep(5)

    mod()

    # Check box
    print(user_name)
    newuser = find('//*[@id="app"]/nav/div/ul/li[4]/a')
    print(newuser.text)
    assert newuser.text == 'remek'

finally:
    driver.close()
