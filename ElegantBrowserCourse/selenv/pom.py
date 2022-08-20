from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
my_driver = webdriver.Chrome(service=s)


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        input_field = self.driver.find_element(By.ID, 'ipt1')
        input_field.clear()
        input_field.send_keys(text)
        return None

    def get_input_text(self):
        input_field = self.driver.find_element(By.ID, 'ipt1')
        input_text = input_field.get_attribute('value')
        return input_text

    def click_submit_button(self):
        button = self.driver.find_element(By.ID, 'b1')
        button.click()
        return None

    def acknowledge_alert(self):
        alert_obj = Alert(self.driver)
        alert_obj.accept()
        return None


# Running Automation

# Giving our Bot a heart
test_page = TrainingGroundPage(driver=my_driver)

# Defininf Test variables
my_input_text = "Baker"

# Performing Test options (Running our Bot)
test_page.go()
test_page.type_into_input(my_input_text)
test_page.click_submit_button()
test_page.acknowledge_alert()
text_from_input = test_page.get_input_text()
assert text_from_input == my_input_text, f"Test Failed: Input text does not match! Expected: {my_input_text} ; " \
                                         f"Actual: {text_from_input}  "
print("Test Passed")
