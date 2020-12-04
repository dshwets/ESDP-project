# Created by daniil at 04.12.2020
Feature: View hostel service list page

  Scenario: Positive view hostel service list page
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens hostel service list page
    And Displays hostel services list page with "{title}" and "{text_name}"