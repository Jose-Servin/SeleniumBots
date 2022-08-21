from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        # "Element finds its self"
        self.find()

    def find(self):
        """
        General: 'wait up to 10 seconds to find the element we are looking for.'
        :return:
        None
        """
        # In Selenium the "locator" is the By paired with the element_location represented as a tuple ()
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator))

        # Populate the web_element with the element we just found
        self.web_element = element
        return None

    def click(self):
        """
        General: 'wait up to 10 seconds to find the element we are looking for and perform a click action.'
        :return:
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    @property
    def text(self):
        """
        Returns the text from a found WebElement element.
        :return:
        """
        element_text = self.web_element.text
        return element_text

    def get_attribute(self, attribute_var):
        attribute = self.web_element.get_attribute(attribute_var)
        return attribute
