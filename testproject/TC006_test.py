# TC006_test - Post comment (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True


def test_comment():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.set_window_size(1000, 500, 500)

    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(2)

    # Enter the data to be uploaded
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'
    comment_text = 'I written a comment to the post'

    # Fields xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    sign_button_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
    sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
    my_title_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
    post_tilte_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1'
    comment_x = '//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/textarea'
    comment_btn_x = '//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/button'
    comment_text_x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]'

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

    # Post view
    driver.find_element(By.XPATH, username_x).click()  # username click
    time.sleep(2)
    driver.find_element(By.XPATH, my_title_x).click()  # my title click
    time.sleep(2)
    driver.find_element(By.XPATH, post_tilte_x).click()  # post title click
    time.sleep(2)

    # Post comment
    driver.find_element(By.XPATH, comment_x).send_keys(comment_text)
    driver.find_element(By.XPATH, comment_btn_x).click()

    # Check
    assert comment_text == driver.find_element(By.XPATH, comment_text_x).text
