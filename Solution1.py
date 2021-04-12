#Verify the search bar autocomplete drop down text.

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
driver.get("https://moat.com/")
time.sleep(10)
Scroll_to_Search= driver.find_element_by_xpath("//div[@class='adsearch__form']")
driver.execute_script("arguments[0].scrollIntoView(true);", Scroll_to_Search)
Click_search = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "adsearch-input")))
Click_search.click()
time.sleep(5)
Send_Text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "adsearch-input")))
Send_Text.send_keys("Saturn")
time.sleep(2)
Verify_AutoText_Visibility = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@Class='auto-complete-text']")))
print(len(Verify_AutoText_Visibility))








