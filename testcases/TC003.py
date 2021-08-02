# TC002 - User log out
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)

try:
    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(2)

    # Enter the data to be uploaded
    email = 'username5555@gmail.com'
    username = 'username5555'
    pwd = 'Username5555'


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
    time.sleep(2)


    # Sign Out
    def sign_out():
        out_button = find('//*[@id="app"]/nav/div/ul/li[5]/a')
        out_button.click()


    sign_out()
    time.sleep(2)

    # Controll
    assert username != find('/html/body').text
    print(username)
    time.sleep(2)


finally:
    driver.close()
