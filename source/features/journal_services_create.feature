Feature: Create JournalService

  Scenario: Create JournalService
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens guest detail page
    And I click on Добавить услугу button
    And Changes hostel service, service executor
    And I press confirm add button