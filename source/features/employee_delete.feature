Feature: Deleting an employee

  Scenario: Delete an employee
    Given There is user with name "admin" and password "admin"
    And There is an employee
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Open employee delete page
    And I press confirm delete employee button
    Then Then I get to employees list page