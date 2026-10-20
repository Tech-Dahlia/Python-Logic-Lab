

# code intro
while True: 
    score = input("Enter your game score (or 'stop' to quit): ")
    cleaned = score.strip().lower() # Remove leading/trailing whitespace or case sensitivity
    print(f"You entered: {score}")

# handling the exit condition first as a rule of thumb.
if cleaned == 'stop':
    print:("Game session ended!")
     break

#the extra stuff 
score = int(cleaned)
    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")
