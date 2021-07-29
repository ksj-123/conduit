# TC001 - User Registration
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)


def find_than_clear(xpath):
    find = driver.find_element_by_xpath(xpath)
    find.clear()
    return find


try:
    driver.get("http://localhost:1667/")


    # Sign up
    def registration_process():
        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
        with open('../text/registration.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                find_than_clear('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(row[0])
                find_than_clear('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(row[1])
                find_than_clear('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input').send_keys(row[2])
        sign_up = driver.find_element_by_xpath('//form/button')
        sign_up.click()


    registration_process()
    print(registration_process())


    # Check box
    assert (driver.find_element_by_xpath("/html/body/div[2]/div/div[3]").text == "Your registration was successful!")
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div/button").click()
    time.sleep(5)

finally:
    driver.close()
