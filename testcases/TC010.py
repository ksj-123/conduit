# TC010 - Global feed is filled with data
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import csv
import pprint
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)


def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


extracted_date = []

try:
    # Oldal betöltése
    driver.get('http://localhost:1667/')
    time.sleep(2)

    # Feltöltendő adatok megadása
    email = 'username5005@gmail.com'
    username = 'username5005'
    pwd = 'Username5005'


    # Driver find
    def find(xpath):
        find = driver.find_element_by_xpath(xpath)
        return find


    # Sign in
    def sign_in(email, pwd):
        sign_button = find('//*[@id="app"]/nav/div/ul/li[2]/a')
        sign_button.click()
        find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
        find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(pwd)
        sign_in_btn = find('//*[@id="app"]/div/div/div/div/form/button')
        sign_in_btn.click()
        time.sleep(2)


    sign_in(email, pwd)
    time.sleep(2)

    # Global feed
    while True:
        time.sleep(2)
        table = find('//*[@id="app"]/div/div[2]')
        rows = table.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]')
        for row in rows:
            data_row = {}
            for i in range:
                cells = row.find_elements_by_xpath(f"//div[{i + 1}]/a/h1")
                data_row['title'] = cells[0].text
                extracted_date.append(data_row)
                for i in next_button:
                    find(f"//li[{i + 1}]/a").click()
                    if not next_button.is_enabled():
                        break
                    else:
                        next_button.click()
                pprint.pprint(extracted_date)
                print(len(extracted_date))


finally:
    pass
    # driver.close()
