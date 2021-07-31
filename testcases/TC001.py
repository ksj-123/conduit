# TC001 - User Registration
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)


def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


try:
    # Oldal betöltése
    driver.get("http://localhost:1667/")


    # Sign up
    def reg():
        find('//*[@id="app"]/nav/div/ul/li[3]/a').click()
        with open('../text/registration.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                print(row)
                find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(row[0])
                find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(row[1])
                find('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input').send_keys(row[2])
        sign_up = find('//form/button')
        sign_up.click()


    reg()
    print(reg)
    time.sleep(5)

    # Check box
    assert ('Welcome!' in find('/html/body/div[2]/div/div[2]').text)
    time.sleep(5)
    find("/html/body/div[2]/div/div[4]/div/button").click()
    time.sleep(5)

finally:
    driver.close()
