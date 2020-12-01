Feature: Delete document from the service executor

  Scenario: Delete document
    Given There is user with name "admin" and password "admin"
    And There is a service executor
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens document in service executor view page
    Then I press delete button on the document
    Then Opens service executor view page