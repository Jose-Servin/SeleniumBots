from selenium.webdriver.common.by import By
from base_page import BasePage
from base_element import BaseElement
from locators import Locator


class TrialPage(BasePage):
    url = "https://techstepacademy.com/trial-of-the-stones"

    @property
    def stone_input(self):
        locator = Locator(by=By.ID, element_location="r1Input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def stone_answer(self):
        locator = Locator(By.ID, 'r1Btn')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def stone_confirm(self):
        locator = Locator(By.CSS_SELECTOR, "div[id='passwordBanner'] > h4")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def secrets_input(self):
        locator = Locator(By.CSS_SELECTOR, "input#r2Input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def secrets_answer(self):
        locator = Locator(By.CSS_SELECTOR, "button#r2Butn")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def secret_confirm(self):
        locator = Locator(By.CSS_SELECTOR, "div[id='successBanner1'] > h4")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def find_wealthy_merchant(self):
        locator = Locator(By.XPATH, "//b[contains(text(), 'Jessica')]")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def merchant_input(self):
        locator = Locator(By.ID, "r3Input")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def merchant_answer(self):
        locator = Locator(By.ID, "r3Butn")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def merchant_confirm(self):
        locator = Locator(By.CSS_SELECTOR, "div[id='successBanner2'] > h4")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def submit_answers(self):
        locator = Locator(By.ID, "checkButn")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def confirmation_text(self):
        locator = Locator(By.CSS_SELECTOR, "div[id='trialCompleteBanner'] > h4")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
