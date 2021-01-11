Feature: View product incomes page

  Scenario: View service executor page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens product incomes view page
    And Displays product incomes fields