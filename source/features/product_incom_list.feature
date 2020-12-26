Feature: Product Income List

  Scenario:Product Income List
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens Product Income list page
    And Displays Product Income list page with "{title}" and "{text_name}"