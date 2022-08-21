from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pom import TrainingGroundPage

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
my_driver = webdriver.Chrome(service=s)

# Run Test
test_page = TrainingGroundPage(driver=my_driver)
test_page.go()
assert test_page.button_1.get_text() == "Button1"
print("All tests complete! ")
