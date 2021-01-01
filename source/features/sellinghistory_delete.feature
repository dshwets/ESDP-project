Feature: Delete product

  Scenario: User with permissions deletes product
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens Selling History list page
    And Displays Selling History list page with "История продаж" and "{text_name}"
    Then I open Sellinghistory delete page
    And I press confirm delete button
    Then Displays empty Selling History list page