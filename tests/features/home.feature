Feature: A List Home Page

Scenario: Edith has heard about a new online to-do app and goes to the homepage.
Given Edith's browser is on the home page
When the title is checked
Then it is the expected title
And she is invited to enter a to-do item

Scenario: Edith enters her first item
Given Edith's browser is on the home page
When Edith enters her first item
Then the page updates and shows her item
And the text box invites her to enter another item

Scenario: Edith enters her next item
Given Edith's browser is on the home page with the first item entered
When Edith enters her second item
Then the page updates and shows her items
And the text box invites her to enter another item

Scenario: Edith checks that her list has been saved
Given Edith's browser is on the home page with a list of items
When Edith navigates to the unique URL for her page
Then the new page has her items
