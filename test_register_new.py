import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create an instance of the WebDriver (you may need to download the appropriate driver for your browser)
driver = webdriver.Chrome()
random_number = random.randint(0, 100000000)
# Open the login page
driver.get("http://localhost:5000/signup")
time.sleep(2)
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("test_email" + str(random_number) + "@example.com")
time.sleep(2)
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(str(random_number))

login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Sign Up')]")
login_button.click()
assert driver.current_url == "http://localhost:5000/login"
# Wait for a few seconds to see the result
driver.implicitly_wait(5)
time.sleep(2)
# Close the browser
# driver.quit()
