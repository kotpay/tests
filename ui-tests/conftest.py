import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def link():
    return "https://skipperprivate.github.io/courseApp/?#"

