from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
driver = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/iframe-training"
driver.get(url=route)

# we are able to be this broad since there is only one iframe element in our webpage.
iframe_location = driver.find_element(By.CSS_SELECTOR, "iframe")

driver.switch_to.frame(iframe_location)

# Find text inside iframe

text_obj = driver.find_element(By.CSS_SELECTOR, "div[id='block-ec928cee802cf918d26c'] > div > p")
print(text_obj.text)

# Take driver back to default content
driver.switch_to.default_content()

# Find title
title_location = "div[id='lower-logo'] > h1 > a"
title_obj = driver.find_element(By.CSS_SELECTOR, title_location)
print(title_obj.text)
