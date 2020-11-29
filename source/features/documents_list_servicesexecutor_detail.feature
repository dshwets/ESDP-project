Feature: View document in service executor page

  Scenario: View document in service executor page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens document in service executor view page
    And Displays docements "{title}"