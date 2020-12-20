Feature: Delete product

  Scenario: User with permissions deletes product
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens hostel product list page
    And Displays product list page with "{product_title}" and "{qty}"
    Then I press delete button
    And I press confirm delete button
    Then Displays empty product list page with title "Список товаров"