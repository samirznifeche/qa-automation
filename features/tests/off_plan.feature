Feature: Tests for Off-Plan feature

  Scenario: User can filter by "Announced"
    Given Open the Sign_In page
    When Login to the page with valid credentials: "**********" and "**********"
    And Click on Off-Plan option
    Then Verify Off-Plan page opens
    When Filter by sale status of "Announced"
    Then Verify each product has "Announced"