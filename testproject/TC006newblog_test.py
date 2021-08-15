# TC006 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from random import randint
import time
import csv

opt = Options()
opt.headless = True


def test_newpost():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(8)

    url_title_list = []

    # Enter the data to be uploaded
    user_name = f"Rapid{randint(1, 99)}"
    user = [user_name, f"{user_name}@gmail.com", 'PassWord@123']

    # Sign up
    driver.find_element(By.XPATH, '//a[@href="#/register"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@placeholder="Username"]').send_keys(user[0])
    driver.find_element(By.XPATH, '//*[@placeholder="Email"]').send_keys(user[1])
    driver.find_element(By.XPATH, '//*[@placeholder="Password"]').send_keys(user[2])
    sign_up = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/form/button')
    sign_up.click()
    time.sleep(5)
    reg_ok = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/button')
    reg_ok.click()
    time.sleep(8)

    # Creat new post
    with open('C:\\Users\\User\\PycharmProjects\\conduit\\post.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            driver.find_element(By.XPATH, '//*[@href="#/editor"]').click()
            time.sleep(8)
            driver.find_element(By.XPATH, '//*[@placeholder="Article Title"]').send_keys(row[0])
            driver.find_element(By.XPATH,
                                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(row[1])
            driver.find_element(By.XPATH,
                                '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea').send_keys(
                row[2])
            driver.find_element(By.XPATH, '//*[@placeholder="Enter tags"]').send_keys(row[3])
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            # url_title_list.append(row[0].replace(" ", "-").lower())
            time.sleep(8)

        assert driver.find_element(By.TAG_NAME, "h1").text == row[0]

    driver.close()
    driver.quit()
