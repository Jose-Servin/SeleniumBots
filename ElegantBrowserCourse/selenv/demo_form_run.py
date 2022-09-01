from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from demo_form import DemoForm

s = Service(
    "/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
my_driver = webdriver.Chrome(service=s)

# Begin Automation

form_bot = DemoForm(driver=my_driver)
form_bot.go()
