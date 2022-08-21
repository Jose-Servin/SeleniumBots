from selenium.webdriver.common.by import By
from base_page import BasePage
from base_element import BaseElement


class TrialPage(BasePage):
    url = "https://techstepacademy.com/trial-of-the-stones"

    @property
    def stone_input(self):
        locator = (By.ID, "r1Input")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def stone_answer(self):
        locator = (By.ID, 'r1Btn')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def stone_confirm(self):
        locator = (By.CSS_SELECTOR, "div[id='passwordBanner'] > h4")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def secrets_input(self):
        locator = (By.CSS_SELECTOR, "input#r2Input")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def secrets_answer(self):
        locator = (By.CSS_SELECTOR, "button#r2Butn")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def secret_confirm(self):
        locator = (By.CSS_SELECTOR, "div[id='successBanner1'] > h4")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    def find_wealthy_merchant(self):
        locator = (By.XPATH, "//b[contains(text(), 'Jessica')]")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def merchant_input(self):
        locator = (By.ID, "r3Input")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def merchant_answer(self):
        locator = (By.ID, "r3Butn")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def merchant_confirm(self):
        locator = (By.CSS_SELECTOR, "div[id='successBanner2'] > h4")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def submit_answers(self):
        locator = (By.ID, "checkButn")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )

    @property
    def confirmation_text(self):
        locator = (By.CSS_SELECTOR, "div[id='trialCompleteBanner'] > h4")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            element_location=locator[1]
        )
