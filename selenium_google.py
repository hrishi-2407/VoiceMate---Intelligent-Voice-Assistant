from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def google_search(query):

    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.NAME, 'q')))

    # Find the search bar and enter your search query
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(query + Keys.ENTER)

    wait.until(EC.presence_of_element_located((By.ID, 'search')))

    try:
        # Try to find Wikipedia snippet
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.kno-rdesc span')))
        element = driver.find_element(By.CSS_SELECTOR, 'div.kno-rdesc span')
        return element.text if element else "Couldn't find the required information"
    
    except:
        # If WIkipedia snippet not found, get the first search result snippet
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g div.VwiC3b')))
        element = driver.find_element(By.CSS_SELECTOR, 'div.g div.VwiC3b')
        return element.text if element else "Couldn't find the required information"
    
    finally:
        time.sleep(1)
        driver.quit()


# s = google_search('personality')
# print(s)





