#******************************************************************************
# Author:           Sam Lane
# Lab:              Lab2
# Date:             7/1/2024
# Description:      Based on several user inputs, this program will tell the
#                   user how much their planned distance will cost, and how
#                   many refuels they will need along the way
# Input:            Fuel economy in mpg. Cost of fuel. Distance to be traveled.
#                   Fuel tank capacity. NB: these inputs are "unitless"
#                   I.E you could use this for fish per hectare if so inclined
# Output:           Cost of fuel for driving a given milage. the number of
#                   refueling stops needed when starting with a full tank.
# Sources:          Practice 2 specifications, Lab 2 instructions,
#                   provided textbook
#******************************************************************************

# Sample Run
#
# User input of 10, 5, 100, and 20
# fuel_economy = 10.00
# cost_of_fuel = 5.00
# planned_distance = 100.00
# tank_size = 20.00
#
# Output produces:
# Your trip will cost you around 50.00 friend!
# On your trip, you will need to fully refuel 0.50 times,
#  assuming you have a full tank at start!
#  If this reads less than 1, that is the current tank fill %.
#


# Variables
fuel_economy = 0.00
cost_of_fuel = 0.00
planned_distance = 0.00
tank_size = 0.00
cost_of_driving = 0.00
refuel_stops = 0.00


# User prompts and inputs
print('''NB: these inputs are "unitless". ''')

print("Enter your vehicle's typical fuel economy:")
fuel_economy = float(input())

print("Enter the cost of fuel:")
cost_of_fuel = float(input())

print("Enter the distance you plan on driving:")
planned_distance = float(input())

print("Enter the tank size of your vehicle")
tank_size = float(input())


# Output 1 aka cost_of_driving
cost_of_driving = float((planned_distance*cost_of_fuel)/fuel_economy)

# Output 2 aka refuel_stops
refuel_stops = float(planned_distance/(tank_size*fuel_economy))

print("Your trip will cost you around",
      '{0:.2f}'.format(cost_of_driving),"friend!")
print("On your trip, you will need to fully refuel",
      '{0:.2f}'.format(float(abs((refuel_stops)-1))),
      "times,\n assuming you have a full tank at start! \n "
      "If this reads less than 1, that is the current tank fill %.")
