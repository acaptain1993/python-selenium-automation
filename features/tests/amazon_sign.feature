# Created by aaron at 6/27/2022
Feature: Manages Amazon Sign In Situations


  Scenario: Logged out user sees sign in page when clicking Orders
  Given Open Amazon Page
  When Click Amazon Orders Link
  Then Verify Sign In Page is Opened
