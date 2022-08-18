from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")

browser = webdriver.Chrome(service=s)

route = "https://www.techlistic.com/p/selenium-practice-form.html"
browser.get(url=route)