#3.	Verify the “Random Brand” link on the search results page is random.

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
time.sleep(5)
driver.get("https://moat.com/advertiser/saturday-s-market")
time.sleep(10)
Random = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Random Brand")))
Random.click()
header_identifier = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@Class='header-info-container']/div[@Class='entity-label']/span[@Class='page-type']")))
First_header=header_identifier.text
print(First_header)
time.sleep(10)
Random_Brand = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Random Brand")))
Random_Brand.click()
header_identifier1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@Class='header-info-container']/div[@Class='entity-label']/span[@Class='page-type']")))
Second_header=header_identifier1.text
print(Second_header)
if str(First_header) != str(Second_header):
    print("Random Result displayed")
else:
    print("Same Result displayed")