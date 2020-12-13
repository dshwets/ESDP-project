Feature: Create hostelservice

  Scenario: Update (edit) hostelservice
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens hostel service create page
    And Changes service_name selling and purchase
    And I press confirm save button
