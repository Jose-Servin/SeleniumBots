from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lxml import etree

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
my_driver = webdriver.Chrome(service=s)

my_driver.get("https://techstepacademy.com/trial-of-the-stones")

merchant_divs = my_driver.find_elements(By.XPATH, "//div/span/..")

# creating our tree HTML parser from lxml module
tree = etree.HTML(my_driver.page_source)
tree_merchant_divs = tree.findall(".//div/span/..")
first_merchant = tree_merchant_divs[0]
first_merchant_name = first_merchant.find('./span/b').text
print(first_merchant_name)
