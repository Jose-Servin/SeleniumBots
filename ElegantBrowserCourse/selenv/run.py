from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest

class RiddleSolver(unittest.TestCase):
    pass

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")

browser = webdriver.Chrome(service=s)

route = "https://techstepacademy.com/training-ground"
browser.get(url=route)


button_path = "//button[@name='butn1']"
button = browser.find_element(By.XPATH, button_path)
button.click()