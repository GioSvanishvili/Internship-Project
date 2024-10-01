Feature: Contact Us page

  Scenario: User can open the Contact us page
    Given Open the main page
    When Log in to the page
    And Click on Main Menu button
    And Click on User Icon
    And Click on Contact us option
    Then Verify that contact us page opens
    And Verify there are at least 4 social media icons
    And Verify 'connect the company' button is available and clickable