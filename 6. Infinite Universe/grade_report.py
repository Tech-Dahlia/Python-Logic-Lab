# project: Grade Report Generator
# author: [Your Name]
# Description: Processes student marks, calculates averages and grades, 
# generates a class report with statistics, and provides a search feature.

# 1. Store students in a dictionary
students = {
    "students": [
        {"name": "Alice", "maths": 85, "english": 78, "science": 92},
        {"name": "Bob", "maths": 67, "english": 74, "science": 80},
        {"name": "Charlie", "maths": 90, "english": 88, "science": 95},
        {"name": "David", "maths": 55, "english": 60, "science": 58},
        {"name": "Eva", "maths": 72, "english": 81, "science": 79}
    ]
}

results = []
# Variables to track class statistics
total_class_marks = 0
highest_mark = 0
lowest_mark = 100
total_students = len(students["students"])

print("--- Processing Student Data ---")

# Use a for loop to iterate over all students and calculate each student’s average
for student in students["students"]:
    name = student["name"]
    maths = student["maths"]
    english = student["english"]
    science = student["science"]
    
    # Calculate average
    average = (maths + english + science) / 3
    
    # 3. Apply grade/status logic
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"
        
    # 4. Build results list
    results.append({
        "name": name,
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })
    
    # Update class statistics
    total_class_marks += average
    
    # Check for highest and lowest
    if average > highest_mark:
        highest_mark = average
    if average < lowest_mark:
        lowest_mark = average

# 5. Calculate class average
class_average = total_class_marks / total_students

# 6. Display formatted class report
print("\n=========================================")
print("          CLASS GRADE REPORT             ")
print("=========================================")
print(f"{'Name':<10} | {'Average':<7} | {'Grade':<5} | {'Status'}")
print("-----------------------------------------")

for res in results:
    print(f"{res['name']:<10} | {res['average']:<7} | {res['grade']:<5} | {res['status']}")

print("-----------------------------------------")
print("CLASS STATISTICS:")
print(f"Class Average: {round(class_average, 2)}%")
print(f"Highest Average: {round(highest_mark, 2)}%")
print(f"Lowest Average: {round(lowest_mark, 2)}%")
print("=========================================\n")

# 7. Use a while loop to search for a student
print("You can now search for a student's results.")
print("Type 'exit' to quit the program.")

while True:
    search_name = input("\nEnter a student's name to search: ").strip()
    
    # Check if the user wants to quit
    if search_name.lower() == 'exit':
        print("Exiting search. Goodbye!")
        break
        
    found = False
    # Loop through our results to find the name
    for res in results:
        if res["name"].lower() == search_name.lower():
            print(f"\nFound: {res['name']}")
            print(f"Average: {res['average']}%")
            print(f"Grade: {res['grade']}")
            print(f"Status: {res['status']}")
            found = True
            break # Exit the for loop early since we found them
            
    if not found:
        print(f"Student '{search_name}' not found in the system. Please try again.")
