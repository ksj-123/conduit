# TC004 - Follow other author
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

try:
    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(2)


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

    # Favourit
    # if
    #     else
    #
    #     for i in range
    #
    #
    # def favor():
        heart = find('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/button')
        heart.click()
        '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[5]/div/button'
        '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/button


    # userek
    '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[6]/div/div/a'
    '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[7]/div/div/a'


    # Check box
    # assert username == find('//*[@id="app"]/nav/div/ul/li[4]/a').text
    # print(username)
    # time.sleep(2)

finally:
    driver.close()
