# seleium web-crawler 

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/mengchiehchiang/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.momoshop.com.tw/main/Main.jsp")
search = driver.find_element_by_id("keyword")
search.send_keys("PS4")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located(By.CLASS_NAME, "popularPrd")
)


button = driver.find_element_by_class_name("popularPrd")
button.click()

time.sleep(5)

# link = driver.find_element_by_link_text("新上市")
# link.click()
subTitle = driver.find_elements_by_class_name("prdName")
for t in subTitle:
    print(t.text)


driver.back
driver.quit()