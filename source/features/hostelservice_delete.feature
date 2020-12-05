Feature: Deleting a hostel service

  Scenario: Delete a hostel service
    Given There is user with name "admin" and password "admin"
    And There is a hostel service
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Open hostel service delete page
    And I press confirm delete hostel service button
    Then Then I get to hostel services list page