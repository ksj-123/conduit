# TC002_test - User log in (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def test_login():
    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(5)

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

    # Sign in
    driver.find_element(By.XPATH, sign_button_x).click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pwd_x).send_keys(pwd)
    driver.find_element(By.XPATH, sign_in_btn_x).click()
    time.sleep(2)

    # Check box
    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)

    driver.close()
    driver.quit()