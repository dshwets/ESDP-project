Feature: Creating new service executor

  Scenario: Create new service executor
    Given I open Homepage
    When Enter username "admin" and password "admin"
    And Click on login button
    And Open create service executor page
    And I enter name "test" and last name "test" and middle name "test"
    And  I press submit button
    Then I get to main page
