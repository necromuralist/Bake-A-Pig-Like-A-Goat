# coding=utf-8
"""Testing A List Home Page."""

# PyPi
from expects import (
    contain,
    expect
)

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
)

from selenium import webdriver

import pytest

# testing
from .fixtures import browser
from ..fixtures import katamari

and_also = then
scenarios("../features/home.feature")

HOME_PAGE = "http://localhost:5000"


# ********** Opening the page? ********** #
# @scenario('features/home.feature', 'Edith has heard about a new online to-do app and goes to the homepage.')
# test_edith_has_heard_about_a_new_online_todo_app_and_goes_to_the_homepage

@given("Edith's browser is on the home page")
def ediths_browser_is_on_the_home_page(browser):
    browser.get(HOME_PAGE)
    return

@when('the title is checked')
def the_title_is_checked(browser, katamari):
    katamari.title = browser.title
    return

@then('it is the expected title')
def it_is_the_expected_title(katamari):
    expect(katamari.title).to(contain("To-Do"))
    return

@and_also('she is invited to enter a to-do item')
def she_is_invited_to_enter_a_todo_item():
    return

# ********** enter items ********** #
# ***** The first item
# @scenario('features/home.feature', 'Edith enters her first item')

# @given("Edith's browser is on the home page")

@when('Edith enters her first item')
def edith_enters_her_first_item():
    return

@then('the page updates and shows her item')
def the_page_updates_and_shows_her_item():
    return

@and_also('the text box invites her to enter another item')
def the_text_box_invites_her_to_enter_another_item():
    return

# ***** The next item
# @scenario('features/home.feature', 'Edith enters her next item')

@given("Edith's browser is on the home page with the first item entered")
def ediths_browser_is_on_the_home_page_with_the_first_item_entered():
    return

@when('Edith enters her second item')
def edith_enters_her_second_item():
    return

@then('the page updates and shows her items')
def the_page_updates_and_shows_her_items():
    return

# @and_also('the text box invites her to enter another item')


# ******************** Edith's Page ******************** #
# @scenario('features/home.feature', 'Edith checks that her list has been saved')

@given("Edith's browser is on the home page with a list of items")
def ediths_browser_is_on_the_home_page_with_a_list_of_items():
    return

@when('Edith navigates to the unique URL for her page')
def edith_navigates_to_the_unique_url_for_her_page():
    return

@then('the new page has her items')
def the_new_page_has_her_items():
    return

