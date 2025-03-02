# browser-use-playground

# Install playwright
playwright install

# Using `browser_use`
`browser_use` is a tool that allows browser automation for testing and scraping. Below is a basic example of how to use `browser_use`:

```python
from browser_use import Browser

# Initialize the browser
browser = Browser()

# Open a web page
browser.open("https://example.com")

# Perform actions on the page
browser.click("#button-id")
browser.type("#input-id", "example text")

# Close the browser
browser.close()
```

For more details, refer to the official `browser_use` documentation.

# Explanation of `demo.py`
The `demo.py` file is an example script that demonstrates how to use `browser_use` to automate tasks in a browser. Below is the content of `demo.py`:

This script initializes a browser, opens a web page, performs some actions on the page, and finally closes the browser.