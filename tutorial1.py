#!/usr/bin/env python
import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = os.environ["CHROMED"]
site = r"https://techwithtim.net"

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
driver.get(site)
print(driver.title)

# search = driver.find_element_by_name("s")
search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # articles = main.find_elements_by_tag_name("article")
    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)
except:
    print("there was an issue searching")
finally:
    driver.quit()
