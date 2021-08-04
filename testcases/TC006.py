# TC006 - Post comment
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Enter the data to be uploaded
email = 'testuser1@example.com'
username = 'testuser1'
pwd = 'Abcd123$'
comment_text = 'I written a comment to the post'

try:
    # Load page
    driver.get('http://localhost:1667/')
    time.sleep(2)


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


    # Post view
    def view():
        find('//*[@id="app"]/nav/div/ul/li[4]/a').click()  # username click
        time.sleep(2)
        find('//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a').click()  # my title click
        time.sleep(2)
        find('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1').click()  # post title click
        time.sleep(2)


    view()
    print(view)
    time.sleep(2)


    # Post comment
    def comment():
        find('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/textarea').send_keys(comment_text)
        find('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/button').click()


    comment()
    print(comment)
    time.sleep(2)

    # Check
    assert comment_text == find('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/p').text
    print(comment_text)



finally:
    driver.close()
