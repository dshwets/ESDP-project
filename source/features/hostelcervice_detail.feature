Feature: View service executor page

  Scenario: View service executor page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens hostel service view page
    And  Displays hostel service "{title}"