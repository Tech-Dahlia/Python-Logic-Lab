"""
Project: Code Logic - Student Grade Classifier
Author: Dahlia Mphalo
Description: A Python program that collects a learner's name and marks for
             three subjects, calculates the average, assigns a letter grade
             (A/B/C/D/F) and a Pass/Fail status using conditionals, flags
             any subject mark below 40 as 'needs intervention', and displays
             a formatted report card.
"""

# Input: Code intro 
name = input("What's your name? ")

subject1 = float(input("Enter your mark for Subject 1: "))
subject2 = float(input("Enter your mark for Subject 2: "))
subject3 = float(input("Enter your mark for Subject 3: "))

# Average: Introducung how we will work on the calculations 
Average_mark = (subject1 + subject2 + subject3) / 3

# Grade arranged from highest → lowest
if Average_mark >= 80:
    grade = "A"
elif Average_mark >= 70:
    grade = "B"
elif Average_mark >= 60:
    grade = "C"
elif Average_mark >= 50:
    grade = "D"
else:
    grade = "F"

# Status is separate decision from grade
if Average_mark >= 50:
    status = "PASSED"
else:
    status = "FAILED"

# Intervention flags (check each subject individually
interventions = []
if subject1 < 40:
    interventions.append("Subject 1")
if subject2 < 40:
    interventions.append("Subject 2")
if subject3 < 40:
    interventions.append("Subject 3")

# --- Report card ---
print("\n" + "=" * 40)
print(f"       REPORT CARD — {name}")
print("=" * 40)
print(f"Subject 1: {subject1:>6.2f}")
print(f"Subject 2: {subject2:>6.2f}")
print(f"Subject 3: {subject3:>6.2f}")
print("-" * 40)
print(f"Average:   {Average_mark:>6.2f}%")
print(f"Grade:     {grade}")
print(f"Status:    {status}")

if interventions:
    print(f" Needs intervention in: {', '.join(interventions)}")
else:
    print("No intervention needed.")

print("=" * 40)
