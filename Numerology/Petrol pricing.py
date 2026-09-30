"""
Project: Trip Planning Calculator
Author:  Dahlia Mphalo
Description:  A Python script that estimates the fuel cost of a road trip. The user enters the journey distance (in kilometres) 
              and the current petrol price per litre. The script assumes the vehicle consumes 1 litre of fuel for every 10 kilometres 
              travelled, then calculates the litres required and multiplies by the price to return the total rand cost, rounded to 
              2 decimal places.
"""

#Input
kilometres = float(input( "How many kilometres do you intend to travel? "))
price_per_litre = float(input ("What is the price per litre of fuel? "))

#Process
liters_needed = kilometres / 10  # Assuming the vehicle consumes 1 litre of fuel for every 10 kilometres
total_cost = round(float(liters_needed * price_per_litre),2)

#Output
print( f"you will need {liters_needed} litres of fuel for your {kilometres} km journey." )
print( f"The total cost of fuel for your journey will be R{total_cost}. because petrol costs R{price_per_litre} per litre" )


