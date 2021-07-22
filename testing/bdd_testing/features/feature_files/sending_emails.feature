Feature: Sending Emails
  Background: The user is on the Login Page
    Given The user is on the Login Page

    Scenario: A user forgot their username and wants an email sent to remind them
      Given The user clicks on Forgot username?

      When The user inputs their first name and last name
      And The user clicks the Resend username button

      Then The user is redirected to a page telling them the username email was sent

    Scenario: A user forgot their username and wants an email sent to reset it
      Given The user clicks on Forgot password?

      When The user inputs their username
      And The user clicks the Reset password button
      And The user enters the OTP
      And The user clicks the Authenticate User button

      Then The user is redirected to a page telling them the password email was sent

    Scenario: A logged in user wants to reset their password
      Given The user logs in
      And The user clicks on Settings

      When The user clicks on the Send email link

      Then The user is redirected to a page telling them the password email was sent again