#4.	Verify the “Share” ad feature (it appears on overlay when hovering over an ad).
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
time.sleep(5)
driver.get("https://moat.com/advertiser/saturday-s-market")
time.sleep(10)
T = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@Class='er-creative-container'][1]")))
time.sleep(10)
#hover to ad
actions = ActionChains(driver)
actions.move_to_element(T)
actions.perform()
time.sleep(10)
#Verify the “Share” ad feature (it appears on overlay when hovering over an ad)
Share_Link=WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@Class=' bottom-of-creative-popup']/div[@Class='share-link']")))
if(Share_Link.is_displayed()):
    print("Share ad feature appears on overlay when hovering over an ad)")
else:
    print("Share ad feature not appears")
