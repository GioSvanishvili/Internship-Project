Feature: Change Password

  Scenario: User can open change password page
    Given Open the main page
    When Log in to the page
    And Click on Settings button
    And Click on Change password button
    Then Verify the change password page opens
    When Add some test password to the input fields
    Then Verify the 'Change password' button is available
