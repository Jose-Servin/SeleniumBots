from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, by, element_location):
        self.driver = driver
        self.by = by
        self.element_location = element_location
        self.elm_locator = (self.by, self.element_location)
        self.web_element = None
        # "Element finds its self"
        self.find()
        self.click()

    def find(self):
        """
        General: 'wait up to 10 seconds to find the element we are looking for.'
        :return:
        None
        """
        # In Selenium the "locator" is the By paired with the element_location represented as a tuple ()
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elm_locator))

        # Populate the web_element with the element we just found
        self.web_element = element
        return None

    def click(self):
        """
        General: 'wait up to 10 seconds to find the element we are looking for and perform a click action.'
        :return:
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.elm_locator))
        element.click()
        return None

    def get_text(self):
        """
        Returns the text from a found WebElement element.
        :return:
        """
        element_text = self.web_element.text
        return element_text
