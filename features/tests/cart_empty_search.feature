# Created by aaron at 6/1/2022
Feature: Checks if Cart is Empty
  # Enter feature description here

  Scenario: Clicking and Checking Cart
    Given Open Amazon page
    When Cart is Clicked
    Then Verify Cart is Empty