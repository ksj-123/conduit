# TC009 - Cookie's
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False

try:

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.set_window_size(1000, 800, 600)
    driver.get("http://localhost:1667/")
    time.sleep(2)

    # Button xpath
    accept_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div'
    declain_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div'
    cookie_bar = '/html/body/div/footer/div/div/div/div/button'


    # Cookie
    def cookie():
        accept_button = driver.find_element_by_xpath(accept_btn)
        assert accept_button.is_enabled()

        declain_button = driver.find_element_by_xpath(declain_btn)
        assert declain_button.is_enabled()

        cookie_bar_buttons = driver.find_elements_by_xpath(cookie_bar)
        print(len(cookie_bar_buttons))
        assert len(cookie_bar_buttons) == 2

        accept_button.click()
        time.sleep(2)

        driver.refresh()

        driver.get("http://localhost:1667/")
        time.sleep(5)

        cookie_bar_buttons = driver.find_elements_by_xpath(cookie_bar)
        print(len(cookie_bar_buttons))
        assert len(cookie_bar_buttons) == 0


    cookie()

finally:
    driver.close()
