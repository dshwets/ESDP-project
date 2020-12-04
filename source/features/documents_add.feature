Feature: Creating new document in service executor

  Scenario: Create new document in service executor
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens document in service executor view page
    And I click on login Добавить Документ
    Then And Changes document title and file
    And I press confirm add button