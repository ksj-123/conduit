# TC007_test - Edit blog post (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True


def test_edit_post():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

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
    my_title_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
    post_tilte_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1'
    title_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
    edit_xp = '//*[@id="app"]/div/div[1]/div/div/span/a'
    tags_btn_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]'
    publish_btn_x = '//*[@id="app"]/div/div/div/div/form/button'

    # Test data
    title_2 = 'Blog mod'
    about_2 = 'Blog'
    write_2 = 'Ez nem mese'
    tags_2 = 'Rémálom'

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

    # Find one of my post
    driver.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(2)

    # Post modification
    driver.find_element(By.XPATH, username_x).click()  # username click
    time.sleep(2)
    driver.find_element(By.XPATH, my_title_x).click()  # my title click
    time.sleep(2)
    driver.find_element(By.XPATH, post_tilte_x).click()  # post title click
    time.sleep(2)
    driver.find_element(By.XPATH, edit_xp).click()  # edit article button click
    time.sleep(2)
    driver.find_element(By.XPATH, title_xp).clear()
    driver.find_element(By.XPATH, title_xp).send_keys(title_2)
    driver.find_element(By.XPATH, about_xp).clear()
    driver.find_element(By.XPATH, about_xp).send_keys(about_2)
    driver.find_element(By.XPATH, write_xp).clear()
    driver.find_element(By.XPATH, write_xp).send_keys(write_2)
    tags_btn = driver.find_element(By.XPATH, tags_btn_x)
    tags_btn.click()
    driver.find_element(By.XPATH, tags_xp).send_keys(tags_2)
    publish_btn = driver.find_element(By.XPATH, publish_btn_x)
    publish_btn.click()

    # Controll
    assert title_2 in (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/h1'))
    assert write_2 in (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p'))
    assert tags_2 in (driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[2]'))
