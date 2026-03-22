Feature: Tests for Off-Plan feature

  Scenario Outline: User can filter by "Sales Status"
    Given Open the Sign_In page
    When Login to the page with valid credentials: "**********" and "**********"
    And Click on Off-Plan option
    Then Verify Off-Plan page opens
    When Filter by sales status of "<status>"
    Then Verify each product has "<status>"
    Examples:
    |status         |
    |Announced      |
    |Start Of Sales |
    |On Sale        |
    |Out of Stock   |