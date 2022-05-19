from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
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

    def check_url(self, url):
        present_url = self.browser.current_url
        assert url in present_url, \
            f"Проверяемый {url} не верный, действующий {present_url}!"

    def element(self, locator):
        return self.browser.find_element(*locator)

    def send_value_by_locator(self, value, locator):
        return self.element(locator).send_keys(str(value))

    def send_value_by_xpath(self, value, locator):
        return self.browser.find_element_by_xpath(locator).send_keys(str(value))

    def clear_by_locator(self, locator):
        return self.element(locator).clear()

    def clear_by_xpath(self, xpath):
        return self.browser.find_element_by_xpath(xpath).clear()

    def is_element_clickable_by_locator(self, locator):
        elem = self.element(locator)
        if elem.is_enabled():
            return False
        else:
            return True

    def is_element_clickable_by_xpath(self, xpath):
        elem = self.browser.find_element_by_xpath(xpath)
        if elem.is_enabled():
            return False
        else:
            return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_attribute_by_locator(self, value, locator):
        try:
            return self.element(locator).get_attribute(f"{value}")
        except NoSuchElementException:
            return None

    def get_attribute_by_xpath(self, value, locator):
        try:
            return self.browser.find_element_by_xpath(f"{locator}").get_attribute(f"{value}")
        except NoSuchElementException:
            return None

    def check_elements(self, list_of_elements):
        for item in list_of_elements:
            assert self.is_element_present(*item), f"Элемент {item} не найден!"

    def check_input_field(self, locator, result):
       assert self.get_attribute_by_locator("innerHTML", locator) == result, \
           f"Значение в поле ввода не совпадает с ожидаемым! fac- {self.get_attribute_by_locator('innerHTML', locator)}, assert - {result}"

    def click_element_by_locator(self, locator):
        self.element(locator).click()

    def click_element_by_xpath(self, xpath):
        self.browser.find_element_by_xpath(xpath).click()
