from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from datetime import datetime
import time, re

class BaseFunction:
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        return self
