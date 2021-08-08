# TC009 - Cookie's
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 800, 600)

# Load page
driver.get("http://localhost:1667/")
time.sleep(3)

# Button xpath
accept_x = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]'
btn_x = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]'

'//*[@id="app"]/footer/div/span/a'


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


try:
    # Cookie
    def cookie():
        accept_btn = find(accept_x)
        assert accept_btn.is_enabled()
        accept_btn.click()
        time.sleep(3)
        driver.back()

        btn_list = find(btn_x)
        assert len(btn_list) == 0


    cookie()

finally:
    driver.close()
