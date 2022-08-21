from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from trial_page import TrialPage

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
my_driver = webdriver.Chrome(service=s)

# Begin Automation
trial_page = TrialPage(driver=my_driver)
trial_page.go()

# First Riddle
trial_page.stone_input.input_text("Rock")
trial_page.stone_answer.click()
first_riddle_ans = trial_page.stone_confirm.text
assert trial_page.stone_confirm.text == "bamboo"

# Second Riddle
trial_page.secrets_input.input_text(first_riddle_ans)
trial_page.secrets_answer.click()
second_riddle_confirmation = trial_page.secret_confirm.text
assert second_riddle_confirmation == "Success!"

# Third Riddle
wealthy_merchant_name = trial_page.find_wealthy_merchant().text
trial_page.merchant_input.input_text(wealthy_merchant_name)
trial_page.merchant_answer.click()
third_riddle_confirmation = trial_page.merchant_confirm.text
assert third_riddle_confirmation == "Success!"

# Final Answer Submitting
trial_page.submit_answers.click()
confirmation_txt = trial_page.confirmation_text.text
assert confirmation_txt == "Trial Complete"

# Proper system resource management
my_driver.quit()

print("All test complete! CONGRATS!!! POM!!! ")
