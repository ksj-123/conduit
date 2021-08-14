# TC006_test - New blog post (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

opt = Options()
opt.headless = True


def test_new_blog():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # Enter the data to be uploaded
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'

    # User xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'

    # Post fields xpath
    title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'

    # Button xpath
    sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    sign_inbtn = '//*[@id="app"]/div/div/div/div/form/button'
    new_artbtn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    publish = '//*[@id="app"]/div/div/div/div/form/button'

    # Sign in
    sign_button = driver.find_element(By.XPATH, sign_btn)
    sign_button.click()
    driver.find_element(By.XPATH, email_x).send_keys(email)
    driver.find_element(By.XPATH, pwd_x).send_keys(pwd)
    sign_in_btn = driver.find_element(By.XPATH, sign_inbtn)
    sign_in_btn.click()
    time.sleep(2)

    assert username == driver.find_element(By.XPATH, username_x).text
    time.sleep(2)

    url_title_list = []

    with open('C:\\Users\\User\\PycharmProjects\\conduit\\post.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            driver.find_element(By.XPATH, new_artbtn).click()
            time.sleep(3)
            driver.find_element(By.XPATH, title_x).send_keys(row[0])
            driver.find_element(By.XPATH, about_x).send_keys(row[1])
            driver.find_element(By.XPATH, write_x).send_keys(row[2])
            driver.find_element(By.XPATH, tags_x).send_keys(row[3])
            driver.find_element(By.XPATH, publish).click()
            url_title_list.append(row[0].replace(" ", "-").lower())
            time.sleep(3)

    # Check URL
    time.sleep(3)
    testuser1_link = driver.find_element(By.XPATH, username_x)
    testuser1_link.click()
    time.sleep(3)

    # Attributes of the created blogs
    # (from index 5 because there is another one created for 'testuser1')
    blogs_href = driver.find_elements(By.XPATH, '//div//a[@class="preview-link"]')
    urls = []
    for b in blogs_href[5:]:
        urls.append(b.get_attribute("href"))

    # Check URL
    for i, j in zip(url_title_list, urls):
        assert f'http://localhost:1667/#/articles/{i}' == j

    driver.close()
    driver.quit()