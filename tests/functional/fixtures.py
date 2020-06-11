# pypi

from pytest import fixture
from selenium import webdriver


class Katamari:
    """Something to stick things into"""


@fixture
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    yield browser
    browser.close()
    return


@fixture
def katamari():
    return Katamari()
