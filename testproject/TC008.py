# TC008 - My blog post delete
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)

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
mytitle_btn_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
posttilte_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1'
delete_btn_x = '//*[@id="app"]/div/div[1]/div/div/span/button/span'
article_preview = '//*[@class="article-preview"]'


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


try:
    # Sign in
    def sign_in(email, pwd):
        sign_button = find(sign_button_x)
        sign_button.click()
        find(email_x).send_keys(email)
        find(pwd_x).send_keys(pwd)
        sign_in_btn = find(sign_in_btn_x)
        sign_in_btn.click()
        time.sleep(2)


    sign_in(email, pwd)
    time.sleep(2)

    # Post find
    find(username_x).click()  # username click
    time.sleep(2)
    find(mytitle_btn_x).click()  # my title click
    time.sleep(2)

    article_number = driver.find_elements_by_xpath(article_preview)
    print(len(article_number))
    original_num = int(len(article_number))


    # Post delete
    def delete():

        find(posttilte_x).click()  # post title click
        time.sleep(2)
        find(delete_btn_x).click()  # delete button click
        time.sleep(2)
        find(username_x).click()  # username click
        time.sleep(2)


    delete()
    print(delete)
    time.sleep(2)

    # Control
    article_number = driver.find_elements_by_xpath(article_preview)
    print(len(article_number))
    new_num = int(len(article_number))
    print(new_num)
    assert new_num + 1 == original_num

finally:
    driver.close()
