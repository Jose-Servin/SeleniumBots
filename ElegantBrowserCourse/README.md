# Elegant Browser Automation with Python and Selenium

This directory holds the code and projects that will be completed as I work through the course 
"Elegant Browser Automation with Python and Selenium".

## Virtual Environment
Created with `python3.9 -m venv .` under the `selenv` directory which holds the virtual environment.

## Finding an element using CSS in the console
To find an element in the console use the structure: `$$("input[id='ipt1']")`
## Finding an element using XPath in the console
To find an element in the console use the structure: `$x("//button[@name='butn1']")`. <br>

By using the XPath, we are able to move up and down the DOM Tree. <br>

If we get into a situation where the only unique identifier is text or some other property, we start at the 
lowest child element and implement the `contains()` function and `text()`.

Final example is: `$x("//b[contains(text(),'Product 1')]")`

To "walk up" the DOM we use `/..` which is the equivalent command for `cd ..`. Therefore, if we take the example 
XPath of our child element and want to move up we use `$x("//b[contains(text(),'Product 1')]/..")`. <br>

To "walk down" the DOM we simply declare the element type `$x("//b[contains(text(),'Product 1')]/../b")`. This 
command is 
saying "start at the unqiue Bold element that contains the text 'Product 1', then walk up the DOM to the `span` and 
then back down to the `b` element."

### Why do this?
This strategy let's us find elements that are NOT unique by first focusing on the unique child element and then 
"walking up" the DOM to locate the element we were really interested in. In the begining, we had two `div` elements 
that were not unique. We searched for "what is unique" AKA "what is the difference between these two elemetns/" 
(This is where the detective work comes in). After finding this UNIQUE element, we walk up to the element we really 
want. Which for this example was the `div`. 