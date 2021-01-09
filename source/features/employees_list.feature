Feature: View employees list page

  Scenario: Positive view employees list page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens employees list page
    And Displays employees list page with "{employee_last_name}"