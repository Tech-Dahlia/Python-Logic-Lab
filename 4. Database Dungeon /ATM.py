"""
Project: Automated Teller Machine (ATM) Simulation
Author:  Dahlia Mphalo
Description:  Simulates an ATM withdrawal. Checks that the requested amount is valid and does not exceed the balance, then updates the
              balance and prints the outcome.

"""

#  ===============
#   DATA STRUCTURE CHEAT SHEET
#   Lists        = [ ]       ordered, changeable (mutable)
#   Dictionaries = { }       key-value pairs, changeable (mutable)
#   Tuples       = ( , )     ordered, unchangeable (immutable).   and The comma is what creates a tuple, not the brackets. edd x(1, 2, 3 )
#  ===============


Balance = int(1000.00) # int because i want the ATM to withdraw in whole number asinput() always returns a string.

Withdrawal = int(input("Enter the amount you'd like to withdraw: ")) #int because the ATM withdraws in whole number 


if Withdrawal <= 0: #is the amount invalid? (zero or negative) Checked FIRST because bad input must never reach the balance.
    print("Amount needs to be more that R 0 and as whole values")
          
elif Withdrawal <= Balance:     #The deduction lives INSIDE this branch on purpose Before the fix, it sat above the if-statement and destroyed
                                # the balance even when the withdrawal failed
    Balance = Balance - Withdrawal
    print (f" Withdrawal successful! Please collect your money R {Withdrawal} Remaining balance: {Balance} " )

else:  #Using 'else' instead of 'elif Withdrawal > Balance' because by elimination, this is the only remaining case.
    print (f"Declined. Insufficient funds your current Balance is R {Balance} please withdraw woithin the range ") 
     # One clear message for print above is better than two repeating the same idea.

