# TC009_test - Cookie's (pytest)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

opt = Options()
opt.headless = True


# Cookie
def test_cookie():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.get("http://localhost:1667/")
    time.sleep(2)

    # Button xpath
    accept_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div'
    declain_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div'
    cookie_bar = '/html/body/div/footer/div/div/div/div/button'
    accept_button = driver.find_element(By.XPATH, accept_btn)
    assert accept_button.is_enabled()

    declain_button = driver.find_element(By.XPATH, declain_btn)
    assert declain_button.is_enabled()

    cookie_bar_buttons = driver.find_elements(By.XPATH, cookie_bar)
    assert len(cookie_bar_buttons) == 2

    accept_button.click()
    time.sleep(2)

    driver.refresh()

    driver.get("http://localhost:1667/")
    time.sleep(2)

    cookie_bar_buttons = driver.find_elements(By.XPATH, cookie_bar)
    assert len(cookie_bar_buttons) == 0
