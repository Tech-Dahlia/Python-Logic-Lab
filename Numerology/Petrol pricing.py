kilometres = float(input( "How many kilometres do you intend to travel? "))
price_per_litre = round(float(input ("What is the price per litre of fuel? ")),2)

litters_needed = kilometres / 10  # Assuming the vehicle consumes 1 litre of fuel for every 10 kilometres
total_cost = litters_needed * price_per_litre

print( f"you will need {litters_needed} litres of fuel for your {kilometres} km journey." )
print( f"The total cost of fuel for your journey will be R{total_cost}. beacuse petrol cosrs R{price_per_litre} per litre" )
