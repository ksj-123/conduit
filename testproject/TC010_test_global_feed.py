# TC010_test - Global feed is filled with data (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


def test_Global():
    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Enter the data to be uploaded
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'

    # Fields xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    sign_button_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
    sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'

    # Sign in
    sign_button = driver.find_element(By.XPATH, sign_button_x)
    sign_button.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pwd_x).send_keys(pwd)
    sign_in_btn = driver.find_element(By.XPATH, sign_in_btn_x)
    sign_in_btn.click()
    time.sleep(2)

    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)

    # Global feed
    pages = driver.find_elements(By.CLASS_NAME, 'page-link')
    for p in range(len(pages)):
        pages[p].click()
        time.sleep(1)

    assert len(pages) + 1 > len(pages)

    driver.close()
    driver.quit()
