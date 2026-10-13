Feature: Invalid Quantity Constraint

  As a shopper
  I want the app to reject invalid quantities
  So that data integrity is maintained

  Background:
    Given I am logged in as a test user

  @negative @boundary
  Scenario Outline: App rejects invalid quantity "<qty>"
    When I search for "iPhone"
    And I add the first product to cart with quantity "<qty>"
    And I open the cart page
    Then the cart should contain 0 items

    Examples:
      | qty  |
      | 0    |
      | -1   |
      | 9999 |

  @boundary @cart
  Scenario: App accepts maximum allowed quantity
    When I search for "iPhone"
    And I add the first product to cart with quantity 10
    And I open the cart page
    Then the cart should contain 1 item
    And the quantity of the first product should be "10"