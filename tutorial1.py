import os
from selenium import webdriver

home_dir = os.path.dirname(os.path.realpath(__name__))
PATH = home_dir + "/chromedriver"
driver = webdriver.Chrome(PATH)
site = "http://www.google.com"

driver.get(site)
