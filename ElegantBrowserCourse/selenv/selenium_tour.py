from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
browser = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
browser.get(url=route)


# Click Button
button = browser.find_element(By.ID, "b1")
button.click()

alert_obj = Alert(browser)
alert_obj.accept()

# Enter Baker and Copy/Paste into second input

browser.find_element(By.ID, "ipt1").send_keys("Baker")

action = ActionChains(browser)
action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
action.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()


