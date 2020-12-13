Feature: Update hostelservice

  Scenario: Update (edit) hostelservice
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens hostel service list page
    And I press update button on the hostelservice
    And Changes service_name selling_price and purchase_price
    And I press confirm save button