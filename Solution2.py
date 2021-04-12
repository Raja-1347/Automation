#2.	Verify the creatives count on the search results page is correct for these 3 search terms: Saturn, Saturday’s Market, and Krux.

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())

def Verify_CreativeCount_Krux():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
    driver.maximize_window()
    time.sleep(5)
    driver.get("https://moat.com/advertiser/Krux")
    time.sleep(10)
    Creative_Count_header_identifier = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@Class='creative-count']/span[1]")))
    Creative_Count_header=Creative_Count_header_identifier.text
    Creative_Count_header_trim =''.join(filter(lambda x: x.isdigit(), Creative_Count_header))
    print(Creative_Count_header_trim)
    time.sleep(2)
    Load = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Load More')]")))
    Load.click()
    time.sleep(5)
    Image_Count = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@Class='er-creative-container' or @Class='er-combined-creative-container']")))
    Total_Image_Count = len(Image_Count)
    print(Total_Image_Count)
    time.sleep(5)
    if str(Creative_Count_header_trim)==str(Total_Image_Count):
        print("Creative Count is equal")
    else:
        print("Creative Count is not equal")

def Verify_CreativeCount_Saturday():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
    driver.maximize_window()
    time.sleep(5)
    driver.get("https://moat.com/advertiser/saturday-s-market")
    time.sleep(10)
    Creative_Count_header_identifier = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@Class='creative-count']/span[1]")))
    Creative_Count_header=Creative_Count_header_identifier.text
    Creative_Count_header_trim =''.join(filter(lambda x: x.isdigit(), Creative_Count_header))
    print(Creative_Count_header_trim)
    time.sleep(5)
    Image_Count = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@Class='er-creative-container' or @Class='er-combined-creative-container']")))
    Total_Image_Count = len(Image_Count)
    print(Total_Image_Count)
    time.sleep(5)
    if str(Creative_Count_header_trim)==str(Total_Image_Count):
        print("Creative Count is equal")
    else:
        print("Creative Count is not equal")

def Verify_CreativeCount_Saturn():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
    driver.maximize_window()
    time.sleep(5)
    driver.get("https://moat.com/advertiser/saturn")
    time.sleep(10)
    Creative_Count_header_identifier = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@Class='creative-count']/span[1]")))
    Creative_Count_header=Creative_Count_header_identifier.text
    Creative_Count_header_trim =''.join(filter(lambda x: x.isdigit(), Creative_Count_header))
    print(Creative_Count_header_trim)
    time.sleep(2)
    for i in range(5):
        Load = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Load More')]")))
        Load.click()
        time.sleep(2)
    time.sleep(5)
    Image_Count = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@Class='er-creative-container' or @Class='er-combined-creative-container']")))
    Total_Image_Count = len(Image_Count)
    print(Total_Image_Count)
    time.sleep(5)
    if str(Creative_Count_header_trim)==str(Total_Image_Count):
        print("Creative Count is equal")
    else:
        print("Creative Count is not equal")


Verify_CreativeCount_Saturday()
Verify_CreativeCount_Krux()


