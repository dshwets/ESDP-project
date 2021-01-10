Feature: View employee create page

  Scenario: View employee create page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then I open  employee create page
    Then I enter title "first_name"
    And I press submit button