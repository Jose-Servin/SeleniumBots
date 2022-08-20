from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
driver = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
driver.get(url=route)

# Open new tab to RealPython
driver.execute_script(
    "window.open('https://realpython.com/','_blank');"
)

# Open new tab to Selenium
driver.execute_script(
    "window.open('https://www.selenium.dev/','_blank');"
)
# Now that we have two tabs open, we use the driver.window_handles attribute
tabs = driver.window_handles
tabs_open = len(tabs)

# Now we can manually switch to different tabs using the switch_to.windows(handles_obj[index])
# By default Selenium behavior, the tabs get assigned indexes based on the order which they load
driver.switch_to.window(tabs[0]) # TechStep loads first
# driver.switch_to.window((tabs[-1])) # RealPython loads last
# driver.switch_to.window(tabs[1])  # Selenium loads second
