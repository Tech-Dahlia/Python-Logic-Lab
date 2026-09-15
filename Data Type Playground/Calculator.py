#Basic Calculator

# Input from user
a = input("Enter the first number: ")
b = input("Enter the second number: ")

# Processing the input and performing calculations
sum = float(a) + float(b)
sub = float(a) - float(b)
div = float(a) / float(b)
Mult = float(a) * float(b)

# Outputting the results
print (f"The sum of {a} + {b} is: {sum}")
print (f"The difference of {a} - {b} is: {sub}")
print (f"The product of {a} * {b} is: {Mult}")
print (f"The quotient of {a} / {b} is: {div}")
