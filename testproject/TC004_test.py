# TC004_test - Follow other author (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True


# Sign in
def test_follow():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.set_window_size(1000, 500, 500)

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

    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(2)

    # Sign in
    sign_button = driver.find_element(By.XPATH, sign_button_x)
    sign_button.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pwd_x).send_keys(pwd)
    sign_in_btn = driver.find_element(By.XPATH, sign_in_btn_x)
    sign_in_btn.click()
    time.sleep(2)

    # Check box
    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)


    # Favourit
    heart = driver.find_element(By.XPATH, heart_x)
    heart.click()

    # Check box
    if driver.find_elements(By.XPATH, '//app[@class="btn btn-sm pull-xs-right btn-primary"]') == []:
        print('favorite selected')
    else:
        print('not selected')
