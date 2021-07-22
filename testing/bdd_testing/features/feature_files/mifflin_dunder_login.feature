Feature: Mifflin Dunder Login

  Background: A user is on the pre login page and would like to login as employee or manager
    Given A user is on the pre login page

    Scenario: A user is on the pre login page and would like to login as an employee
      Given The user clicks on the Login as employee link
      And The user enters the correct username and password as employee
      And The user clicks submit button as employee

      When The user enters the OTP as employee
      And The user clicks the Authenticate User button as employee

      Then The user is redirected to their employee profile

    Scenario: A user is on the pre login page and would like to login as a manager
      Given The user clicks on the Login as manager link
      And The user enters the correct username and password as manager
      And The user clicks submit button as manager

      When The user enters the OTP as manager
      And The user clicks the Authenticate User button as manager

      Then The user is redirected to their manager profile