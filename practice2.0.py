#******************************************************************************
# Author:           Sam Lane
# Lab:              Practice2
# Date:             7/1/2024
# Description:      This program will ask a user for their vehicles fuel
#                   economy in mpg(miles per gallon), as well as the cost
#                   of fuel without specifying currency. User inputs can
#                   be floating numbers.
#                   The program will output the cost of driving 20,
#                   75, and 500 miles respectively.
# Input:            Fuel economy in mpg. Cost of fuel
# Output:           Cost of fuel for driving a given milage.
# Sources:          Practice 2 specifications, provided textbook
#******************************************************************************

# Sample run.
# User input of 10 mpg and 5 dollars per gallon of fuel would output:
# 10 dollars for 20 miles, 37.5 dollars for 75 miles, 250 dollars for 500 miles
# You don't need to include these three lines in your program!


# Variables
fuel_economy = 0.00
cost_of_fuel = 0.00
cost_of_driving = 0.00
x=20.00
y=75.00
z=500.00

# User prompts and inputs
print("Enter your vehicle's typical fuel economy")
fuel_economy = float(input())

print("Enter the cost of fuel")
cost_of_fuel = float(input())

# Output aka cost_of_driving
cost_of_driving = float((x*cost_of_fuel)/fuel_economy)
cost_of_driving1 = float((y*cost_of_fuel)/fuel_economy)
cost_of_driving2 = float((z*cost_of_fuel)/fuel_economy)
print("The cost of driving 20 miles is", '{0:.2f}'.format(cost_of_driving))
print("The cost of driving 75 miles is", '{0:.2f}'.format(cost_of_driving1))
print("The cost of driving 500 miles is", '{0:.2f}'.format(cost_of_driving2))
