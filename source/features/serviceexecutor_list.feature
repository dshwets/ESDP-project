# Created by aizhan at 28/11/20
Feature: View service executor list page

  Scenario: Positive view service executor list page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens service executor list page
    And Displays serviceexecutor list page with "{title}"
