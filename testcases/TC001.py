# TC001 - User Registration
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://react-layr-realworld-example-app.layrjs.com/all")

    def register(username, email, password):
        driver.get("http://localhost:1667/#/")
        driver.find_element_by_xpath('//*[@id="root"]/div/nav/div/ul/li[3]/a').click()
        with open('registration.csv') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                username = find_and_clear_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/fieldset[1]/input').send_keys(row[0])
                email = find_and_clear_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/fieldset[2]/input').send_keys(row[1])
                password = find_and_clear_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/fieldset[3]/input').send_keys(row[2])
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/form/fieldset/button').click()

    # leellenőrizni, hogy a regisztrált username megjelenik a jobb felső sarokban
    # assert

finally:
    driver.close()
