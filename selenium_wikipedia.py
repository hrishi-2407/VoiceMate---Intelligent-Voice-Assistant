from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")

wait1 = WebDriverWait(driver, 3)
wait1.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]')))

# Find the search bar and enter your search query
search_box = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
search_box.send_keys("Obama")

wait2 = WebDriverWait(driver, 3)
wait2.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-form"]/fieldset/button/i')))

# Find the search button and click it
search_button = driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button/i')
search_button.click()

time.sleep(5)

driver.quit




