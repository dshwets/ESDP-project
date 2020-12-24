Feature: Selling History List

  Scenario: Selling History List
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens Selling History list page
    And Displays Selling History list page with "{title}" and "{text_name}"