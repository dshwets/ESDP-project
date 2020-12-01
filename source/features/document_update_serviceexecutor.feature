Feature: Update document from the service executor

  Scenario: Update (edit) document
    Given There is user with name "admin" and password "admin"
    And There is a service executor
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens document in service executor view page
    Then I press update button on the document
    And Changes document title and file
    And I press confirm save button