# The idea of a "base page" is to describe all things that a page, in general, should be able to do.
# This is not specific to a website, but rather the actions behind each bot.
# What are the common behaviors my Monster needs?

class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

# TODO add refresh functionality to BasePage
