#Final project - 4th Draft



from budget_cashTRACKS import Month

# from user_guided_menu import *

# from user_guided_menu_detail import *

from user_guided_menu_full import *

import csv

# month = raw_input("Current Month: ")
# year = raw_input("Current Year: ")
# my_month = Month(month, year) 

#if dont have file, then ask if want to create new budget
#if have file, ask if want to edit budget/add transaction

menu = (
	"1. Create Budget",
	"2. View This Month's Budget",
	"3. Add Transactions for This Month",
	"4. Track This Month's Spending Goals",
	"5. Exit"
		)

print "\n"

print "CA$H TRACKS"

print "\n"


while (True):
	for choice in menu:
		print choice
	user_choice = raw_input("Choose desired action by selecting it's corresponding number: ")
	if (user_choice == "5") or (str.upper(user_choice) == "EXIT"): 
		exit()
	elif user_choice == "1":
		option_create_budget()
	elif user_choice == "2":
		option_view_current_budget()
	elif user_choice == "3":
		option_add_transaction()
	elif user_choice == "4":
		option_track_budget_spending_goals()
	elif  user_choice not in ("1" , "2", "3", "4"):
		print "Woops! Please choose which action by selecting it's cooresponding number."
		



# my_month_budget_data = []

# my_month_expenditure_data = []

# my_month_budget_spending_tracker_data = []


file_save()

###############








