from selenium.webdriver.common.by import By
from base_element import BaseElement
from base_page import BasePage
from locators import Locator


class TrainingGroundPage(BasePage):
    url = "https://techstepacademy.com/training-ground"

    @property
    def button_1(self):
        btn_locator = Locator(By.ID, "b1")
        return BaseElement(
            driver=self.driver,
            locator=btn_locator
        )
