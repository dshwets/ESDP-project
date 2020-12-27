Feature: Update JournalService

  Scenario: Create JournalService
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens journal service update page
    And editing data