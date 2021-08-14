# TC004_test - User data modification(pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random import randint
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

def test_username_mod():
    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(2)

    # Fields xpath
    sign_up_btn = '//*[@id="app"]/nav/div/ul/li[3]/a'
    username_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input'
    sign_up_x = '//*[@id="app"]/div/div/div/div/form/button'
    o_btn = '/html/body/div[2]/div/div[4]/div'
    setting_x = '//*[@href="#/settings"]'
    usernamex = '//*[@placeholder="Your username"]'
    update_btn = '//*[@id="app"]/div/div/div/div/form/fieldset/button'
    oke_btn = '/html/body/div[2]/div/div[3]/div/button'
    new_user_link = '//*[@id="app"]/nav/div/ul/li[4]/a'

    # Enter the data to be uploaded
    user_name = f"Rapid{randint(1, 99)}"
    user = [user_name, f"{user_name}@gmail.com", 'PassWord@123']
    new_username = 'remek'


    # Sign up
    driver.find_element(By.XPATH, sign_up_btn).click()
    time.sleep(5)
    driver.find_element(By.XPATH, username_x).send_keys(user[0])
    driver.find_element(By.XPATH, email_x).send_keys(user[1])
    driver.find_element(By.XPATH, pwd_x).send_keys(user[2])
    sign_up = driver.find_element(By.XPATH, sign_up_x)
    sign_up.click()
    time.sleep(5)
    reg_ok = driver.find_element(By.XPATH, o_btn)
    reg_ok.click()
    time.sleep(5)

    # Settings - username modification
    driver.find_element(By.XPATH, setting_x).click()
    time.sleep(2)
    username = driver.find_element(By.XPATH, usernamex)
    username.clear()
    username.send_keys(new_username)
    driver.find_element(By.XPATH, update_btn).click()
    time.sleep(5)
    driver.find_element(By.XPATH, oke_btn).click()
    time.sleep(5)

    # Check box
    print(user_name)
    newuser = driver.find_element(By.XPATH, new_user_link)
    print(newuser.text)
    assert newuser.text == 'remek'


    driver.close()
    driver.quit()
