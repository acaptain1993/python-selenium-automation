# Created by aaron at 6/1/2022
Feature: Confirm User is On Cancel Order Page


  Scenario: Verify Cancel Order Page
    Given Open Amazon Customer Service
    When Cancel Order is Searched
    Then Confirm Cancel Order is On Screen