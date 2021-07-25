# New blog post
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    def sign_in(email, password):
        driver.get("https://react-layr-realworld-example-app.layrjs.com/all")
        driver.find_element_by_link_text('Sign in').click()
        email = driver.find_element_by_tag_name('Email').send_keys('username1@gmail.com')
        password = driver.find_element_by_tag_name('Password').send_keys('Username1')
        driver.find_element_by_class_name('btn').click()
    sign_in('user1@gmail.com', 'User1')

    # driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/ul/li[2]/a').click()
    # with open('post.csv') as csvfile:
    #     csvreader = csv.reader(csvfile, delimiter=',')
    #     next(csvreader)
    #     for row in csvreader:
    #         print(row)
    #         title = driver.find_element_by_tag_name('Article title').send_keys(row[0])
    #         about = driver.find_element_by_tag_name("What's this article about?").send_keys(row[1])
    #         write = driver.find_element_by_link_text('Write your article (in markdown)').send_keys(row[2])
    #         tags = driver.find_element_by_name('Enter tags').send_keys(row[3])
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/form/fieldset/button').click()
    # time.sleep(2)

finally:
    pass
    # driver.close()
