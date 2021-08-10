# TC009 - Cookie's
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 800, 600)
driver.get("http://localhost:1667/")
time.sleep(2)

# Button xpath
accept_x = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]'
btn_x = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]'
accept_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div'
declain_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div'
cookie_bar = '//*[@id="cookie-policy-panel"]/div'

assert accept_btn.is_enabled()
assert declain_btn.is_enabled()

# ha elfogadjuk (accept) '//*[@id="app"]/footer/div/span'
# ha elutasítjuk (declain) '//*[@id="app"]/footer/div/span'
# learn more... '//*[@id="cookie-policy-panel"]/div/div[1]/div/a'
#         https://www.cookiesandyou.com/


# Driver find
def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find


try:
    # Cookie
    def cookie():
        driver.get("http://localhost:1667/")
        time.sleep(2)
        accept_btn = find(accept_x)
        time.sleep(2)
        assert accept_btn.is_enabled()
        time.sleep(2)
        accept_btn.click()
        time.sleep(2)
        driver.close()

        driver.get("http://localhost:1667/")
        time.sleep(2)
        btn_list = find(btn_x)
        assert len(btn_list) == 0


    cookie()

finally:
    driver.close()
