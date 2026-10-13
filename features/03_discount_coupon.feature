Feature: Discount Coupon Validation

  As a shopper
  I want to apply coupon codes at checkout
  So that I receive the correct discount

  Background:
    Given I am logged in as a test user
    And I have added "iPhone" to cart with quantity 1

  @positive @coupon
  Scenario: Apply a valid coupon
    When I open the checkout page
    And I apply the coupon "SAVE10"
    Then the coupon should be accepted
    And the discount should not be "-$0.00"

  @negative @coupon
  Scenario: Apply an expired coupon
    When I open the checkout page
    And I apply the coupon "EXPIRED2020"
    Then the coupon should be rejected
    And the discount should be "-$0.00"

  @negative @coupon
  Scenario: Apply an invalid coupon
    When I open the checkout page
    And I apply the coupon "FAKE123"
    Then the coupon should be rejected
    And the discount should be "-$0.00"

  @smoke @order
  Scenario: Place an order successfully
    When I open the checkout page
    And I place the order
    Then I should land on the orders page
    And I should see at least 1 order