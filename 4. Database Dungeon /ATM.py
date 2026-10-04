"""
Project: Automated Teller Machine (ATM) Simulation
Author:  Dahlia Mphalo
Description:  Simulate a bank transaction checking 

"""

#  ===============
#   DATA STRUCTURE CHEAT SHEET
#   Lists        = [ ]       ordered, changeable (mutable)
#   Dictionaries = { }       key-value pairs, changeable (mutable)
#   Tuples       = ( , )     ordered, unchangeable (immutable).   and The comma is what creates a tuple, not the brackets. edd x(1, 2, 3 )
#  ===============


Balance = int(1000.00)

Withdrawal = int(input("Enter the amount you'd like to withdraw: ")) #int because the ATM withdraws in whole number 


if Withdrawal <= 0:
    print("Amount needs to be more that R 0 and as whole values")
          
elif Withdrawal <= Balance: 
    Balance = Balance - Withdrawal
    print (f" Withdrawal successful! Please collect your money R {Withdrawal} Remaining balance: {Balance} " )

else:
    print (f"Insufficient funds your current Balance is R {Balance} please withdraw woithin the range ")

    print("Declined. Insufficient funds")
