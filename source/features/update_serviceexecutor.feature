Feature: Update service executor

  Scenario: Редактирование исполнителя услуг
    Given There is user with name "admin" and password "admin"
    When I open Homepage
    Then I enter username "admin" and password "admin"
    And I click on login button
    Then Opens create service executor page
    Then I enter name "test" and last name "test" and middle name "test"
    And I press submit button
    Then Открыть страницу редактирования исполнителья услуг
    Then И ввести имя "test_update_name" фамилия "test_update_last" и отчество "test_update_middle"
    And И нажимаю на кнопку сохранить
