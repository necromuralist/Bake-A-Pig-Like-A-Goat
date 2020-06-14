Feature: Home Page functions

Scenario: Retrieve the home page HTML
  Given a call to the root URL
  When the title is checked
  Then the HTML has the expected title
