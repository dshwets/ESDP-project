Feature: Selling history update

  Scenario: Selling history update
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens Selling history update page
    And editing data Selling history
    And I press confirm save button