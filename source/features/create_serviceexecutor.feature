Feature: Creating new service executor

  Scenario: Create new service executor
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens create service executor page
    Then I enter name "test" and last name "test" and middle name "test"
    And I press submit button
    Then Opens main page
