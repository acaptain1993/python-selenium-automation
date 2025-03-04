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
#HW5
  Scenario: Cycle Through Product Color Options
    Given Product B081YS2F7N Page
    Then Click and Verify Each Color Option
#HW8
  Scenario: Use Drop Down, Change Department, Search for Item
    Given Open Amazon Page
    Then Change Department to Software
    When Search for Windows 11
    Then Verify Current Department

  Scenario: Open Product Page, Hover New Arrivals, Verify Deals
    Given Product B074TBCSC8 Page
    Then New Arrivals Hovered
    Then Verify Deals Present


