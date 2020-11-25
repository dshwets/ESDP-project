Feature: Login page

    Scenario: Login to AppleHostel with valid parameters
        Given I open Homepage
        When Enter username "admin" and password "admin"
        And Click on login button
        Then User must have successfully login to the Guest list page with "{text}"
