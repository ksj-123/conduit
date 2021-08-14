# TC007 - Post comment
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)

# Load page
driver.get('http://localhost:1667/')
time.sleep(2)


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


# Enter the data to be uploaded
email = 'testuser1@example.com'
username = 'testuser1'
pwd = 'Abcd123$'
comment_text = 'I written a comment to the post'

# Fields xpath
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
sign_button_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
my_title_x = '//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a'
post_tilte_x = '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1'
comment_x = '//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/textarea'
comment_btn_x = '//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/button'
comment_text_x = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/p'

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


    # Post view
    def view():
        find(username_x).click()  # username click
        time.sleep(2)
        find(my_title_x).click()  # my title click
        time.sleep(2)
        find(post_tilte_x).click()  # post title click
        time.sleep(2)


    view()
    time.sleep(2)


    # Post comment
    def comment():
        find(comment_x).send_keys(comment_text)
        find(comment_btn_x).click()


    print(comment_text)
    comment()
    time.sleep(2)

    # Check
    assert comment_text == find(comment_text_x).text
    print(comment_text)



finally:
    driver.close()
