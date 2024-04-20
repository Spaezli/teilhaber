from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver
chrome_driver_path = './chromedriver'

# Set up the ChromeDriver
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()

# Initialize the driver
driver = webdriver.Chrome(service=service, options=options)

# Function to scroll to the bottom of the page
def scroll_to_bottom():
    old_position = driver.execute_script("return window.scrollY")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # wait for more items to load
        new_position = driver.execute_script("return window.scrollY")
        if new_position == old_position:
            break
        old_position = new_position

# Navigate to the webpage
driver.get("https://www.hinto.ch/de/events-20.html?page=1#paginator-a")

# Wait for the page to load and then scroll to the bottom
scroll_to_bottom()

# Wait until all elements are loaded
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ht-event")))

# Collect all elements with the class 'ht-event'
events = driver.find_elements(By.CLASS_NAME, "ht-event")

# Extract information from the elements
event_list = [event.text for event in events]

# Print the results
for event in event_list:
    print(event)

# Close the driver
driver.quit()
