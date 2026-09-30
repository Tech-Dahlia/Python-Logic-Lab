kilometres = float(input( "How many kilometres do you intend to travel? "))
price_per_litre = float(input ("What is the price per litre of fuel? "))

litters_needed = kilometres / 10  # Assuming the vehicle consumes 1 litre of fuel for every 10 kilometres

print( f"you will need {litters_needed} litres of fuel for your {kilometres} km journey." )
