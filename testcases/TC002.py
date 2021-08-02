# TC002 - User registration (sign up) - User log out - User log in
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Enter the data to be uploaded
email = 'username5555@gmail.com'
username = 'username5555'
pwd = 'Username5555'

try:
    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(2)


    # Sign up
    def reg():
        reg_button = find('//*[@id="app"]/nav/div/ul/li[3]/a')
        reg_button.click()
        find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(username)
        find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(email)
        find('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input').send_keys(pwd)
        sign_up = find('//form/button')
        sign_up.click()


    reg()
    print(reg)
    time.sleep(3)

    # Sign out
    find('/html/body/div[2]/div/div[4]/div/button').click()
    time.sleep(5)
    find('//*[@id="app"]/nav/div/ul/li[5]/a').click()
    time.sleep(3)


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
    time.sleep(2)

    # Check box
    assert username == find('//*[@id="app"]/nav/div/ul/li[4]/a').text
    print(username)
    time.sleep(2)

finally:
    driver.close()
