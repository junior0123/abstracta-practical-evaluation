Feature: Purchase a product

  @purchase @test_01
  Scenario: Successfully purchase a product
    Given the user is on the homepage
    And the user is logged in with valid credentials
    When the user selects the product "Sony xperia z5" from the product listing
    And the user adds the product to the cart
    And the user navigates to the Cart section
    And the user proceeds to the checkout
    And the user enters valid test data for the purchase
    Then the user should see a confirmation message with the order details

  @cart @test_02
  Scenario: Cart retains product after logout and login
    Given the user is on the homepage
    And the user is logged in with valid credentials
    When the user selects the product "HTC One M9" from the product listing
    And the user adds the product to the cart
    And the user logs out
    And the user logs in again with valid credentials
    And the user navigates to the Cart section
    Then the product "HTC One M9" should still be in the cart

  @cart @test_03
  Scenario: Verify the removal of a product from the cart
    Given the user is on the homepage
    And the user is logged in with valid credentials
    When the user selects the product "Sony xperia z5" from the product listing
    And the user adds the product to the cart
    And the user goes back to the product listing
    And the user selects the product "HTC One M9" from the product listing
    And the user adds the product to the cart
    And the user navigates to the Cart section
    And the user removes the product "Sony xperia z5" from the cart
    Then the cart should no longer contain the "Sony Xperia Z5" product
    And the cart should only contain the "HTC One M9" product
