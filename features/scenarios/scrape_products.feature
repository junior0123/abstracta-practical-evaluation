Feature: Scrape product information
  @test_04 @scrape
  Scenario: Scrape product data from the first two pages
    Given the user is on the homepage
    And the user is logged in with valid credentials
    When the user navigates to and scrapes product information from the first "2" pages
    Then the user saves the product information to a text file
