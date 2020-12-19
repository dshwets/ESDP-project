Feature: View product list page

  Scenario: Positive view product list page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens hostel product list page
    And Displays product list page with "{product_title}" and "{qty}"