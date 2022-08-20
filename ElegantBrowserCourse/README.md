# Elegant Browser Automation with Python and Selenium

This directory holds the code and projects that will be completed as I work through the course 
"Elegant Browser Automation with Python and Selenium".

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
driver.switch_to.window(tabs[0]) # TechStep loads first
# driver.switch_to.window((tabs[-1])) # RealPython loads last
# driver.switch_to.window(tabs[1])  # Selenium loads second
```

## Handling IFrames and Frames

If you are having trouble finding an element and have gone through the following checks:
* Located the element in the console and checked it was unique. 
* There are no time delays being applied that cause the element to be hidden when the Bot runs.

The next step to take is to search for the `iframe` element in the HTML. We do this by seaching for `iframe` in the 
HTML using our dev tools console. 