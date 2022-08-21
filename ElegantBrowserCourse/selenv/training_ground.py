from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage


class TrainingGroundPage(BasePage):
    url = "https://techstepacademy.com/training-ground"

    @property
    def button_1(self):
        btn_locator = (By.ID, "b1")
        return BaseElement(
            driver=self.driver,
            by=btn_locator[0],
            element_location=btn_locator[1]
        )
