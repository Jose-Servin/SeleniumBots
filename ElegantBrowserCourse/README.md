# Elegant Browser Automation with Python and Selenium

This directory holds the code and projects that will be completed as I work through the course
"Elegant Browser Automation with Python and Selenium". <br>

Reminders to future me:

* When working with selenium, put on your detective hat.
* You are a detective who is building your own Frankenstein.
* Work slow and THINK.
* Approach all problems with a strategy in mind.
* Use your toolbelt.
* If you can't find an element, walk to it.
* Write code that is Readable "with an R".
* Web Automation should be FUN!

## Virtual Environment

Created with `python3.9 -m venv .` under the `selenv` directory which holds the virtual environment.

## Python Interactive Shell

Use an interactive shell so we can see where in our process the code is at and/or catch errors. <br>
`python -i file.py`

## How to find an element using CSS in the console

To find an element in the console use the structure: `$$("input[id='ipt1']")`.
A shortcut if using the `id` attribute is to use the `#` (hash). To move down to a child element while using css
selectors we use the syntax `div[id='id3'] > h4`.

## How to find an element using XPath in the console

To find an element in the console use the structure: `$x("//button[@name='butn1']")`. <br>

By using the XPath, we are able to move up and down the DOM Tree. <br>

If we get into a situation where the only unique identifier is text or some other property, we start at the
lowest child element and implement the `contains()` function and `text()`.

Final example is: `$x("//b[contains(text(),'Product 1')]")`. <br>
We can also simply use `$x("//b[text() = 'Product 1']")`

To "walk up" the DOM we use `/..` which is the equivalent command for `cd ..`. Therefore, if we take the example
XPath of our child element and want to move up we use `$x("//b[contains(text(),'Product 1')]/..")`. <br>

To "walk down" the DOM we simply declare the element type `$x("//b[contains(text(),'Product 1')]/../b")`. This
command is
saying "start at the unqiue Bold element that contains the text 'Product 1', then walk up the DOM to the `span` and
then back down to the `b` element." <br>

XPath is the strategy to use when you are matching on "text".

### Why do this?

This strategy let's us find elements that are NOT unique by first focusing on the unique child element and then
"walking up" the DOM to locate the element we were really interested in. In the begining, we had two `div` elements
that were not unique. We searched for "what is unique" AKA "what is the difference between these two elemetns/"
(This is where the detective work comes in). After finding this UNIQUE element, we walk up to the element we really
want. Which for this example was the `div`.

## How to Copy and Paste with Selenium

We can see the general structure of a copy and paste function with selenium by using:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
browser = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
browser.get(url=route)
# Enter Baker and Copy/Paste into second input
browser.find_element(By.ID, "ipt1").send_keys("Baker")
action = ActionChains(browser)
action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
action.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
```

## How to use Expected Conditions and WebDriverWait

For this example, we are going to wait until we see an alert on our screen and print out statements that will track
where in our code we are located. This demonstrated the correct way to use WebDriverWait and EC so we don't rely on
time.sleep() functions. <br>

The use of a `WebDriverWait` is called an "explicit wait" because we are telling the WebDriver what to wait for. On
the other end we have "implicit wait" which is us telling the WebDriver "no matter what, wait x seconds."

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
browser = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
browser.get(url=route)
print("Bot arrived to website")
print("Waiting for Alert....")

# Define WebDriverWait and EC
# We will wait until an alert shows up on the page
WebDriverWait(browser, 10).until(EC.alert_is_present())
print("Alert appeared!")
```

## How to deal with Alerts

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
browser = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
browser.get(url=route)

# Click Button
button = browser.find_element(By.ID, "b1")
button.click()

alert_obj = Alert(browser)
alert_obj.accept()
```

## How to navigate the drop-down

A drop down in HTML language is really a `select` element. Therefore, to interact with such element we use the
`selenium.webdriver.support.select` class.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
browser = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
browser.get(url=route)

drop_down_locator = browser.find_element(By.ID, "sel1")
# We create the Select object ON the select element that holds the child elements we want to interact with.
drop_down = Select(drop_down_locator)
# To actually see the options we use call the options attribute that returns a list of child elms under the select tag
# here, we make sure to grab only the text, otherwise we would get objects that are not readable. 
drop_down_options = [i.text for i in drop_down.options]
print(drop_down_options)

# Select second element "Beets"
drop_down.select_by_index(1)

# Assert element was selected based on text
selected_option = drop_down.first_selected_option

assert selected_option.text == 'Beets'
```

## How to handle browser Windows and Tabs

To handle multiple windows, we need multiple WebDriver objects. In essence, we are creating one connection for each
webpage we want to visit. This script shows the basic strategy of how to open multiple browser windows.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
browser_1 = webdriver.Chrome(service=s)
route_1 = "https://techstepacademy.com/training-ground"
browser_1.get(url=route_1)

browser_2 = webdriver.Chrome(service=s)
route_2 = "https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select"
browser_2.get(route_2)
```

From researching, I was able to creat this simple framework to switch to a new tab, bring driver to new tab and
print out the title's.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
driver = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
driver.get(url=route)

# Open new tab to RealPython
driver.execute_script(
    "window.open('https://realpython.com/','_blank');"
)

# Now that we have two tabs open, we use the driver.window_handles attribute
tabs = driver.window_handles
tabs_open = len(tabs)

# Now let's navigate to each tab and print out it's title
# we use the size of the tabs_open to iterate
# we use the tabs object to actually navigate to the tab
for i in range(tabs_open):
    driver.switch_to.window(tabs[i])
    print(driver.title)
```

NOTE: Tabs are not indexed in the order they appear on the browser. They are indexed based on the time it takes to
load on the browser. For the code below, TechStep loaded first, so it is index 0, Selenium loads second, so it is
index 1 and RealPython loads last, so it is -1 index.

The video showed this strategy:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
driver = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/training-ground"
driver.get(url=route)

# Open new tab to RealPython
driver.execute_script(
    "window.open('https://realpython.com/','_blank');"
)

# Open new tab to Selenium
driver.execute_script(
    "window.open('https://www.selenium.dev/','_blank');"
)
# Now that we have two tabs open, we use the driver.window_handles attribute
tabs = driver.window_handles
tabs_open = len(tabs)

# Now we can manually switch to different tabs using the switch_to.windows(handles_obj[index])
# By default Selenium behavior, the tabs get assigned indexes based on the order which they load
driver.switch_to.window(tabs[0])  # TechStep loads first
# driver.switch_to.window((tabs[-1])) # RealPython loads last
# driver.switch_to.window(tabs[1])  # Selenium loads second
```

## Handling IFrames and Frames

If you are having trouble finding an element and have gone through the following checks:

* Located the element in the console and checked it was unique.
* There are no time delays being applied that cause the element to be hidden when the Bot runs.

The next step to take is to search for the `iframe` element in the HTML. We do this by seaching for `iframe` in the
HTML using our dev tools console.

NOTE: While working with iframes, we realized if we couldn't find an object that was unique. Therefore, we walked
down to it with CSS the same way we walk up using xpath. We found the unique identifier for the parent object and walked
down to the p element.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
driver = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/iframe-training"
driver.get(url=route)

# we are able to be this broad since there is only one iframe element in our webpage.
iframe_comp = driver.find_element(By.CSS_SELECTOR, "iframe")

# Taking our driver inside the iframe to make it's component visible to us
driver.switch_to.frame(iframe_comp)

# Find text inside iframe
text_obj = driver.find_element(By.CSS_SELECTOR, "div[id='block-ec928cee802cf918d26c'] > div > p")
print(text_obj.text)
```

### How to go back to the default page

Now that you've navigated inside the iframe and retrieved the information you were looking for, you need to go back
to Base Page. Back to the default page that the driver first came into contact with.

To do this, we use `default_content()`.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
driver = webdriver.Chrome(service=s)
route = "https://techstepacademy.com/iframe-training"
driver.get(url=route)

# we are able to be this broad since there is only one iframe element in our webpage.
iframe_location = driver.find_element(By.CSS_SELECTOR, "iframe")

driver.switch_to.frame(iframe_location)

# Find text inside iframe

text_obj = driver.find_element(By.CSS_SELECTOR, "div[id='block-ec928cee802cf918d26c'] > div > p")
print(text_obj.text)

# Take driver back to default content
driver.switch_to.default_content()

# Find title
title_location = "div[id='lower-logo'] > h1 > a"
title_obj = driver.find_element(By.CSS_SELECTOR, title_location)
print(title_obj.text)
```

## Selenium Page Objects

What are Page Objects? Classes.

These classes contain useful portions of a webpage presented in readable code format.

On the other end of the spectrum, Page Objects can create unnecessary and confusing levels of abstraction therefore
they must be done well and with patience.

END GOAL: <br>
To create automations that in their final run form, can be read by someone who has no exposure to code.

Step 1: <br>
What is your scope? What actions are you trying to automate? What elements do you want to interact with? Translate
that into code.

Example Project: <br>
The scope of this project is

* Navigate to website.
* input text into Input field
* Press Button1

### Building a POM skeleton

Step 1: Describe the page you are viewing.

* What is the name of the page?
* What actions are you doing on what element? Use VERB_NOUN naming convention if possible.

```python
class TrainingGroundPage:
    def __int__(self):
        pass

    def type_into_input(self, text):
        pass

    def get_input_text(self):
        pass

    def click_submit_button(self):
        pass
```

Step 2: Being assembling your webpage Bot.
In their most basic forms, POM can have this simple structure.

```python
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
assert text_from_input == my_input_text, f"Test Failed: Input text does not match! Expected: {my_input_text} ; "
f"Actual: {text_from_input}  "
print("Test Passed")
```

Congratulations! You've created your own baby Frankenstein.

## Selenium POM Part 2 ("middle form")

For part two we are going to upgrade our Bot and give it better structure and a nicer framework. There are three
pages we use to achieve this.

1. run.py
2. pom.py (represents our web page in OOP Form)
3. base_element.py (represents the elements in our webpage in OOP Form)

run.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from training_ground import TrainingGroundPage

s = Service("/Users/joseservin/SeleniumBots/ElegantBrowserCourse/selenv/driver/chromedriver")
my_driver = webdriver.Chrome(service=s)

# Run Test
test_page = TrainingGroundPage(driver=my_driver)
test_page.go()
assert test_page.button_1.get_text() == "Button1"
print("All tests complete! ")
```

pom.py

```python
from selenium.webdriver.common.by import By
from base_element import BaseElement


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self):
        self.driver.get(self.url)

    @property
    def button_1(self):
        btn_locator = (By.ID, "b1")
        return BaseElement(
            driver=self.driver,
            by=btn_locator[0],
            element_location=btn_locator[1]
        )
```

base_element.py

```python
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
```

This current state is a bit confusing since it represent a mix of "unofficial" inheritance and broad separation.
I am having trouble seeing how the dots connect using this "middle" framework BUT none-the-less, our new Bot
has taken a greater form and is closer to its final form which is following a true Selenium POM Framework.

## Selenium POM Final Form

Final POM structure is contained in:

* base_element.py
* base_page.py
* trial_page.py
* run_trial_page.py

## Better Locators

