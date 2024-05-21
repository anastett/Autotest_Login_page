import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def run_test():
    # Create an instance of the WebDriver (you may need to download the appropriate driver for your browser)
    driver = webdriver.Chrome()

    # Open the login page
    driver.get("http://localhost:5000/login")
    time.sleep(2)
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("123@mail.ru")
    time.sleep(2)
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("123")

    remember_me_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    remember_me_checkbox.click()
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_button.click()
    # Wait for a few seconds to see the result
    driver.implicitly_wait(5)
    assert driver.current_url == "http://localhost:5000/profile"

    # Close the browser
    driver.quit()
