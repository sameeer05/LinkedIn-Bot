import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver = Service("**chromedriver location**")
driver = webdriver.Chrome(service=chrome_driver)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WT=2%2C1%2C3&geoId=115884833&keywords=software%20engineer&location=Gurugram%2C%20Haryana%2C%20India")
driver.maximize_window()
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
time.sleep(3)
username.send_keys("**my linkedin username**")
password.send_keys("my linkedin password")
password.send_keys(Keys.ENTER)
time.sleep(3)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
apply_button.click()
submit_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button")
submit_button.click()


