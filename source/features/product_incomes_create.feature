Feature: Creating new product and new product incomes

  Scenario: Create new product and new product incomes
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens productincomes create page
    And i input product barcode
    And I fill out the form with data
#    Then I enter title "test" and last qty "10"
#    And I confirm button