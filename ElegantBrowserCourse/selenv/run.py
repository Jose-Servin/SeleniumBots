from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")

browser = webdriver.Chrome(service=s)

route = "https://techstepacademy.com/trial-of-the-stones"
browser.get(url=route)

# Riddle One
riddle_one_input_location = "input[id='r1Input']"
riddle_one_input = browser.find_element(By.CSS_SELECTOR, riddle_one_input_location)
riddle_one_input.send_keys("Rock")
riddle_one_button_locator = "button[id='r1Btn']"
riddle_one_button = browser.find_element(By.CSS_SELECTOR, riddle_one_button_locator)
riddle_one_button.click()

# Riddle Two
answer_locator = "//h4[contains(text(),'bamboo')]"
answer = browser.find_element(By.XPATH, answer_locator).text

riddle_two_input_location = "input[id='r2Input']"
riddle_two_input = browser.find_element(By.CSS_SELECTOR, riddle_two_input_location)
riddle_two_input.send_keys(answer)
riddle_two_button_locator = "button[id='r2Butn']"
riddle_two_button = browser.find_element(By.CSS_SELECTOR, riddle_two_button_locator)
riddle_two_button.click()

# Riddle Three
merchants = {}

# First merchant
merchant_1_name_locator = "//b[contains(text(),'Jessica')]"
merchant_1_name = browser.find_element(By.XPATH, merchant_1_name_locator).text
merchants['merchant_1_name'] = merchant_1_name

merchant_1_wealth_locator = "//p[contains(text(), '3000')]"
merchant_1_wealth = browser.find_element(By.XPATH, merchant_1_wealth_locator).text
merchants['merchant_1_wealth'] = merchant_1_wealth

# Second Merchant
merchant_2_name_locator = "//b[contains(text(),'Bernard')]"
merchant_2_name = browser.find_element(By.XPATH, merchant_2_name_locator).text
merchants['merchant_2_name'] = merchant_2_name

merchant_2_wealth_locator = "//p[contains(text(), '2000')]"
merchant_2_wealth = browser.find_element(By.XPATH, merchant_2_wealth_locator).text
merchants['merchant_2_wealth'] = merchant_2_wealth

print(merchants)


def which_merchant():
    if int(merchants['merchant_1_wealth']) > int(merchants['merchant_2_wealth']):
        wealthy_merchant = merchants['merchant_1_name']
    else:
        wealthy_merchant = merchants['merchant_2_name']

    return wealthy_merchant


# Riddle Three Answer
riddle_three_locator = "input[id='r3Input']"
riddle_three_answer = browser.find_element(By.CSS_SELECTOR, riddle_three_locator)
riddle_three_answer.send_keys(which_merchant())

riddle_three_button_locator = "button[id='r3Butn']"
riddle_three_button = browser.find_element(By.CSS_SELECTOR, riddle_three_button_locator)
riddle_three_button.click()

# Final Submit
final_button_locator = "button[id='checkButn']"
final_button = browser.find_element(By.CSS_SELECTOR, final_button_locator)
final_button.click()

# Final assert
expected_message = 'Trial Complete'
final_message_locator = "//h4[contains(text(), 'Trial Complete')]"
final_message = browser.find_element(By.XPATH, final_message_locator).text
assert final_message == expected_message
