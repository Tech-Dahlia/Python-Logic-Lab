"""
Project: Game Score Board
Author: Dahlia Mphalo
Description: A Python program that continuously asks for a game score until the player types
             'stop', then shuts down cleanly. 
"""

# code intro
while True: 
    score = input("Enter your game score (or 'stop' to quit): ")
    cleaned = score.strip().lower() # Remove leading/trailing whitespace or case sensitivity
    print(f"You entered: {score}")

    if cleaned == 'stop':
        print:("Game session ended!")
        break

#the extra stuff 
score = int(cleaned)

if score > 100:
   print("Wow! That's a new high score!")    
else:
   print("Good try, keep playing!")
