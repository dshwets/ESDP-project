Feature: Create ProductIncomes form

  Scenario: add product info in form
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens productincomes create page
    And i input product barcode
    And Displays product add form