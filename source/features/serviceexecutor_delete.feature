Feature: Deleting a service executor

  Scenario: Delete a service executor
    Given There is user with name "admin" and password "admin"
    And There is a service executor
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Open service executor detail page
    Then I press delete button
    And I press confirm delete button
    Then Then I get to Homepage