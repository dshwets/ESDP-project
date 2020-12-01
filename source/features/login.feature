Feature: Login page

    Scenario: Login to AppleHostel with valid parameters
        Given There is user with name "admin" and password "admin"
        When I open Homepage
        And I enter username "admin" and password "admin"
        And I click on login button
        Then User must have successfully login to the Guest list page with "{text}"
