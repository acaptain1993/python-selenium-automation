# Created by aaron at 6/24/2022
Feature: Amazon based Test Cases
  # Enter feature description here
  #HW6 updated version
  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original window
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original