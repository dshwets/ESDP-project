Feature: Creating new product

  Scenario: Create cart and make a purchase
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then I Open sell items page
    Then I enter product "123456" and  qty "10"
    And I press submit button
    Then I pess delete good from cart button
