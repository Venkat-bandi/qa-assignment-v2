Feature: Add to Cart

  As a logged-in user
  I want to add products to my cart
  So that I can purchase them

  Background:
    Given I am logged in as a test user

  @smoke @cart
  Scenario: Add a product to the cart and verify count
    When I search for "iPhone"
    And I add the first product to cart with quantity 1
    And I open the cart page
    Then the cart should contain 1 item
    And the cart should display "iPhone"

  @regression @cart
  Scenario: Add multiple different products to the cart
    When I search for "iPhone"
    And I add the first product to cart with quantity 1
    And I open the products page
    And I search for "MacBook"
    And I add the first product to cart with quantity 1
    And I open the cart page
    Then the cart should contain 2 items

  @regression @cart
  Scenario: Update quantity of an existing product in cart
    When I search for "iPad"
    And I add the first product to cart with quantity 2
    And I open the cart page
    Then the cart should contain 1 item
    And the quantity of the first product should be "2"