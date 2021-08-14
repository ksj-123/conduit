# TC005 - Follow other author
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
email = 'testuser1@example.com'
username = 'testuser1'
pwd = 'Abcd123$'

# Fields xpath
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
sign_button_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
heart_x = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/button'  # First heart symbol

try:
    # Load page
    URL = driver.get('http://localhost:1667/')
    time.sleep(2)


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

    # Check box
    assert username == find(username_x).text
    print(username)
    time.sleep(2)


    # Favourit
    def favourit():
        heart = find(heart_x)
        heart.click()


    favourit()

    # Check box
    if driver.find_elements_by_xpath('//app[@class="btn btn-sm pull-xs-right btn-primary"]') == []:
        print('favorite selected')
    else:
        print('not selected')

finally:
    driver.close()
