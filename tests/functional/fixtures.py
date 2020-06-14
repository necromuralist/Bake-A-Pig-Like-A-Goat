# pypi

from pytest import fixture
from selenium import webdriver

@fixture
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    yield browser
    browser.close()
    return

