

# code intro
while True: 
    score = input("Enter your game score (or 'stop' to quit): ")
    cleaned = score.strip().lower() # Remove leading/trailing whitespace or case sensitivity
    print(f"You entered: {score}")
