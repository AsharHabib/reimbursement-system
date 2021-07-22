Feature: Employee Requests

  Background: An employee is logged in and on the profile page
    Given An employee is logged in and on the profile page

    Scenario: An employee would like to check all their sent reimbursement requests
      When An employee clicks on the Reimbursement Requests link
      Then The employee is redirected to the Reimbursement Requests page

    Scenario: An employee would like to submit a new reimbursement request via the input form
      Given An employee is on the Reimbursement Requests page

      When The employee clicks on the Submit new reimbursement request link
      And The employee fills in the Amount and Reason fields
      And The employee clicks on the Submit Request button

      Then The employee is redirected to the Reimbursement Requests page
      And The new reimbursement request is added to the page
      And The employee can delete the new reimbursement

    Scenario: An employee would like to submit a new reimbursement request via uploading a file
      Given An employee is on the Reimbursement Requests page

      When The employee clicks on the Submit new reimbursement request link
      And The employee uploads a file
      And The employee clicks on the Upload File button

      Then The employee is redirected to the Reimbursement Requests page
      And The new reimbursement request is added to the page
      And The employee can delete the new reimbursement