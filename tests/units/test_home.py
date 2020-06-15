# coding=utf-8
"""Home Page functions feature tests."""
# python
from http import HTTPStatus

# pypi
from bs4 import BeautifulSoup

from expects import (
    contain,
    end_with,
    equal,
    expect,
    start_with
)

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
)

# testing
from .fixtures import client
from ..fixtures import katamari

from goatpig import HOME_PAGE, TITLE

scenarios("../features/home_units.feature")

# Check the title
#@scenario('features/home_units.feature', 'Retrieve the home page HTML')
#def test_retrieve_the_home_page_html():


@given('a call to the root URL')
def a_call_to_the_root_url(client, katamari):
    katamari.response = client.get(HOME_PAGE)
    return


@when('the title is checked')
def the_title_is_checked(katamari):
    katamari.data = katamari.response.data.decode("utf-8")
    katamari.soup = BeautifulSoup(katamari.data, "html.parser")
    return


@then('the HTML has the expected title')
def the_html_has_the_expected_title(katamari):
    expect(katamari.response.status_code).to(equal(HTTPStatus.OK))
    expect(katamari.data).to(start_with("<!doctype html>"))
    expect(katamari.soup.title.string).to(equal(TITLE))
    expect(katamari.data).to(end_with("</html>"))
    return

