Feature: Delete journal service

  Scenario: User with permissions deletes journal service
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then I open journalservice view page
    And  It displays "{title}"
    Then I press delete button
    And I press confirm delete button
    Then Displays empty journal service list page with title "Журнал услуг"