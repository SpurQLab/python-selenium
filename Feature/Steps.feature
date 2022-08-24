
Feature: BMI calculator test 1
  Scenario:BMI(Body Mass Index)
#  Given  User is on BMI calculator page
    When User Enters Age 20
    And User clicks on Gender Male
    And User Enters Height 180
    And User Enters Weight 60
    And User clicks on Calculate button
    Then User verify the result 18.5

  Scenario:BMI(Body Mass Index 2)
##  Given  User is on BMI calculator page
    When User Enters Age 35
    And User clicks on Gender Male
    And User Enters Height 160
    And User Enters Weight 55
    And User clicks on Calculate button
    Then User verify the result 21.5

  Scenario:BMI(Body Mass Index 3)
##  Given  User is on BMI calculator page
    When User Enters Age 50
    And User clicks on Gender Male
    And User Enters Height 175
    And User Enters Weight 65
    And User clicks on Calculate button
    Then User verify the result 21.2

  Scenario:BMI(Body Mass Index 2)
##  Given  User is on BMI calculator page
    When User Enters Age 45
    And User clicks on Gender Male
    And User Enters Height 150
    And User Enters Weight 52
    And User clicks on Calculate button
    Then User verify the result 23.1