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
deposit = int(input("Please enetr the amount you'd lijke to deposit: "))

amount_withdrawn  = int (Balance - Withdrawal)
amount_deposited = (Balance + Withdrawal)

if Withdrawal <= Balance: 
    print (f" Withdrawal successful! Please collect your money R {Withdrawal} Remaining balance: {amount_withdrawn} " )

elif withdrawal > Balance:
    print (f"Insufficient funds your current Balance is R {Balance} please withdraw woithin the range ")

elif Balance <= 0:
    print ("Your account is empty, please deposit money to continue using the ATM") 

else:
    print (“ Declined, Insufficient funds”)
 

