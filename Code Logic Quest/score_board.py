

# code intro
while True: 
    score = input("Enter your game score (or 'stop' to quit): ")
    cleaned = score.strip().lower() # Remove leading/trailing whitespace or case sensitivity
    print(f"You entered: {score}")

# handling the exit condition as a rule of thumb.
if cleaned == 'stop':
    print:("Game session ended!")
     break
