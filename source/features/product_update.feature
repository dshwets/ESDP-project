Feature: Update product

  Scenario: Update (edit) product
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens hostel product list page
    And I press update button on the product
    And Changes title and qty product
    And I confirm button