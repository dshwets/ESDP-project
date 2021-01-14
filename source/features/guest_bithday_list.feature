Feature: View Guest birthday list page

  Scenario: Positive view Guest list page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens Guest birthday list page
    And Displays guest birthday list page with "guest"