# Created by aaron at 5/16/2022
Feature: Test for Amazon search

  Scenario: Verify that user can search for coffee
    Given Open Amazon page
    When Search for coffee
    Then Verify search results for coffee are shown
# Hw4 Question 1
  Scenario: Verify 5 Links on Best Seller Page
    Given Best Sellers Amazon
    Then Verify 5 Links Present
#HW4 Question 2
  Scenario: Add Dad Hat to Cart
    Given Open Amazon Page
    When Search for Dad Hat
    Then Click Champion Hat
    And Add it to Cart
    And Cart is Clicked
    And Verify Hat is There
