from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Merchant:
    def __init__(self, merchant_div):
        self.name = merchant_div.find('./span/b').text
        self.wealth = int(merchant_div.find('./p').text)


class PageWithMerchants:
    def __init__(self, page_source):
        self.tree = etree.HTML(page_source)

    def get_merchants(self):
        # the locator for the common parent element (div in our case)
        locator = ".//div/span/.."
        merchant_divs = self.tree.findall(locator)
        return [Merchant(merchant_div=merchant) for merchant in merchant_divs]

    def sort_merchant_high_to_low(self):
        # we use the key + lambda because we are sorting by fields of an object.
        return sorted(self.get_merchants(), key=lambda x: x.wealth, reverse=True)

    def find_wealthiest_merchant(self):
        return self.sort_merchant_high_to_low()[0]


if __name__ == "__main__":
    # defining our driver using Selenium
    s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
    my_driver = webdriver.Chrome(service=s)
    my_driver.get("https://techstepacademy.com/trial-of-the-stones")
    # lxml part starts here
    html = my_driver.page_source
    merchant_page = PageWithMerchants(html)
    wealthiest_merchant = merchant_page.find_wealthiest_merchant()
    print(f"The wealthiest merchant is {wealthiest_merchant.name} with ${wealthiest_merchant.wealth}")
