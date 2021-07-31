try:
    def test_sign_in(email, password):
        driver.get("http://localhost:1667/#/")
        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
            'first@gmail.com')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('First12345')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
        time.sleep(3)
​
        your_feed_btn = driver.find_element_by_class_name('nav-link')
​
        assert your_feed_btn.is_enabled()
​
​
    test_sign_in('first@gmail.com', 'First12345')
​
finally:
    driver.close()