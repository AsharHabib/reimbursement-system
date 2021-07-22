Feature: Manager Specific Functions
  Background: A manager is logged in and on the profile page
    Given A manager is logged in
    And The manager is on the profile page

    Scenario: A manager would like to check all of their employees' requests
      When A manager clicks on the Reimbursement Requests link
      Then The manager is redirected to the Reimbursement Requests page

    Scenario: A manager would like to change the status and message for a request
      Given A manager is on the Reimbursement Requests page

      When The manager changes the status for a request
      And The manager adds an optional message
      And The manager clicks the form button

      Then The manager is redirected to the Reimbursement Requests page
      And The updates are reflected for the particular request

    Scenario: A manager would like to create a new employee account
      Given A manager is on the Sign Up page

      When The manager inputs all the new account's information
      And The manager clicks on the signup button

      Then The manager is redirected to the Profile page
      And The new employee is listed
      And The manager can delete the new employee from the list

    Scenario: A manager would like to view the statistics on their employees' requests
      When A manager clicks on the Statistics link
      Then The manager is redirected to the Statistics page