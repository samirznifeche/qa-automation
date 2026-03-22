Feature: Tests for Community feature

  Scenario: User can open the Community page
    Given Open the Sign_In page
    When Login to the page with valid credentials: "samirznifeche@gmail.com" and "HabibiOlya@76"
    And Click on Settings option
    And Click on Community option
    Then Verify Community page opens
    And Verify the “Contact support” button is available and clickable