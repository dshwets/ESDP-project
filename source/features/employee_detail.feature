
Feature: View employee detail page

  Scenario: View employee detail page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then I open  employee detail page
    And  Displays employee with "{employee_name}"