Feature: Contact Us page

  Scenario: User can open the Contact us page
    Given Open the main page
    When Log in to the page
    And Click on settings option
    And Click on Contact us option
    Then Verify the right page opens
    And Verify there are at least 4 social media icons
    And Verify 'connect the company' button is available and clickable