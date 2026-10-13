Feature: Register and Login

  As a new user
  I want to register and then log in
  So that I can access the shop

  @smoke @register
  Scenario: Register a new user and log in successfully
    Given I open the register page
    When I register with a unique email and password "Test@123"
    Then I should be redirected to the login page
    When I log in with the registered credentials
    Then I should land on the products page

  @negative @login
  Scenario: Login fails with wrong password
    Given I open the login page
    When I log in with email "testuser@shop.com" and password "WrongPass123"
    Then I should see an error message