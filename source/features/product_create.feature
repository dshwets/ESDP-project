Feature: Creating new product

  Scenario: Create new product
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens create product page
    Then I enter title "test" and last qty "10"
    And I press submit button
