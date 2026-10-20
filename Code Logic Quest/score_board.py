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

    # Check for the exit word FIRST, before int() can crash on "stop"
    if cleaned == 'stop':
        print("Game session ended!")
        break

    #the extra stuff (now INSIDE the loop, so it runs every round)
    score = int(cleaned)

    if score > 100:
        print("Wow! That's a new high score!")    
    else:
        print("Good try, keep playing!")
