"""
Project: Multi-Function Calculator
Author: Dahlia Mphalo
Description: This Python calculator called Scientific calculator.py that takes two numbers as input and performs all four basic 
             arithmetic operations plus two advanced operations. The calculator must handle user input safely using type 
             casting and display results clearly using f-strings.

Requirements
Use float(input()) to collect two numbers from the user
Calculate and display: addition, subtraction, multiplication, division
Calculate and display: floor division (//) and modulus (%)
Round all results to 2 decimal places using round()
Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
Display all results in a formatted table using f-strings
"""

# ============================================================
#
# LESSONS LEARNED some reinforced as i knew them but they slipped my mind while coding this mini project initially(read these first):
#
#
# 1. round() is a FUNCTION, not a method.
#    ❌ Wrong:  addition.round(2)
#    ✅ Right:  round(addition, 2)
#    The number goes INSIDE the parentheses, not after a dot.
#
# 2. py_compile only checks SYNTAX, not LOGIC.
#    Silence from `python3 -m py_compile Calculator.py` = "grammar is fine."
#    It does NOT catch:
#       - Division by zero
#       - Calling round() on None
#       - Wrong logic / wrong variable
#       - Type errors
#    Always test with `python3 Calculator.py` and real numbers.
#
# 3. Python runs TOP to BOTTOM. You must CHECK BEFORE you DIVIDE.
#    If you write `division = num_1 / num_2` before the zero check,
#    the crash happens before the safety net is even reached.
#    Fix: put the division math INSIDE the `else` branch.
#
# 4. None is Python's "there is no value here."
#    We set results to None in the zero-case so the variables still
#    EXIST for later printing (otherwise → NameError).
#    Then we guard the print with `if num_2 != 0:` so we never
#    try to round(None) — that would raise a TypeError.
#
# ============================================================


# ---------- STEP 1: Collect input safely ----------
# float(input(...)) = type casting. input() always returns a string,
# so we wrap it in float() to do math on it.
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))


# ---------- STEP 2: Operations that never fail ----------
# Addition, subtraction, multiplication are safe for any two floats.
addition       = num_1 + num_2
subtraction    = num_1 - num_2
multiplication = num_1 * num_2


# ---------- STEP 3: Check BEFORE dividing ----------
# Python runs top-to-bottom. If we divided first and checked after,
# a 0 would crash us before we ever reached the safety net.
if num_2 == 0:
    # ---- Division would be impossible: skip the math ----
    print("Division by zero is not allowed, try another number.")
    # Set the variables to None so they still EXIST for later prints.
    # (If we skipped defining them, the print lines would raise NameError.)
    division        = None
    floor_division  = None
    modulus         = None
else:
    # ---- Safe: num_2 is not zero, so divide ----
    division        = num_1 / num_2     # normal division → float
    floor_division  = num_1 // num_2    # floor division → whole part
    modulus         = num_1 % num_2     # remainder


# ---------- STEP 4: Print results with f-strings ----------
# f-strings let us drop variables straight into a string with {}.
# We wrap each result in round(x, 2) to keep 2 decimal places.
print(f"The sum of {num_1} + {num_2} is: {round(addition, 2)}")
print(f"When Subtracting: {num_1} - {num_2} we get: {round(subtraction, 2)}")
print(f"When doing Multiplication {num_1} x {num_2} we get: {round(multiplication, 2)}")

# Guard the division prints: only run if num_2 was NOT zero.
# Otherwise we'd be doing round(None, 2) → TypeError crash.
if num_2 != 0:
    print(f"Division: {num_1} / {num_2} = {round(division, 2)}")
    print(f"Floor Division: {num_1} // {num_2} = {round(floor_division, 2)}")
    print(f"Modulus: {num_1} % {num_2} = {round(modulus, 2)} which is the remainder")
