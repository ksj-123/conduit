# New blog post
import csv

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://react-layr-realworld-example-app.layrjs.com/all")
    time.sleep(3)


    def signin(email, password):
        driver.find_element_by_link_text('Sign in').click()
        with open('registration.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                email = driver.find_element_by_tag_name('Email').send_keys(row[1])
                password = driver.find_element_by_tag_name('Password').send_keys(row[2])
                signin(email, password)
            driver.find_element_by_class_name('btn').click()
        signin(email, password)
    time.sleep(2)


    def new_post(title, about, write, tags):
        driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/ul/li[2]/a').click()
        with open('post.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                title = driver.find_element_by_tag_name('Article title').send_keys(row[0])
                about = driver.find_element_by_tag_name("What's this article about?").send_keys(row[1])
                write = driver.find_element_by_link_text('Write your article (in markdown)').send_keys(row[2])
                tags = driver.find_element_by_name('Enter tags').send_keys(row[3])
                new_post(title, about, write, tags)
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/form/fieldset/button').click()
        new_post(title, about, write, tags)
    time.sleep(2)

finally:
    pass
    # driver.close()
