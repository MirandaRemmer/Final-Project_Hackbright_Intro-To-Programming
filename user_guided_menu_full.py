#USER-GUIDED MENU  --> ALL PUT TOGETHER

from budget_cashTRACKS import Month

import csv

#my_month = Month("March", "2016")  #creating object MARCH: instantiating an instance of the class Month  
									#USER CHOOSES WHICH MONTH (have the months listed out - user chooses which Month to select??)

##TO CREATE NEW DATA
# my_month = Month(month, year) 
# month = raw_input("Current Month: ")
# year raw_input("Current Year: ")


##TO FIND OLD DATA
# my_month = Month(month, year) 
# month = raw_input("Month: ")
# year raw_input("Year: ")




my_month_budget_data = []


my_month_expenditure_data = []


my_month_budget_spending_tracker_data = []



month = raw_input("Current Month: ")
year = raw_input("Current Year: ")
my_month = Month(month, year) 


def edit_budget_by_cateogry():
	budget_items = (
			"1. Rent", 
			"2. Utilities",
			"3. Transportation",
			"4. Food & Dining", 
			"5. Bars", 
			"6. Shopping", 
			"7. Personal", 
			"8. Health & Fitness",
			"9. Entertainment",
			"10. Travel",
			"11. Medical",
			"12. Savings",
			"13. Return to home"
			)
	while (True): 
		for category in budget_items:
			print category
		user_choice = raw_input("Choose which budget category to edit by selecting it's corresponding number: ")
	
		if (user_choice == "13") or (str.upper(user_choice) == "HOME"):  #option 15: return home
			None
	
		elif user_choice == "1":    #ADD Rent
			rent = float(raw_input("Rent Budget: "))
			my_month.set_budget_value('Rent', rent)

		elif user_choice == "2":    #ADD Utilities
			utilities = float(raw_input("Utilities Budget: "))
			my_month.set_budget_values('Utilities', utilities)
	
		elif user_choice == "3":    #ADD Transportation
			transportation = float(raw_input("Transportation Budget: "))
			my_month.set_budget_values('Transportation', transportation)
	
		elif user_choice == "4":    #ADD Food & Dining
			food_dining = float(raw_input("Food & Dining Budget: "))
			my_month.set_budget_values('Food & Dining', food_dining)
	
		elif user_choice == "5":    #ADD Bars
			bars = float(raw_input("Bars Budget: "))
			my_month.set_budget_values('Bars', bars)
	
		elif user_choice == "6":    #ADD Shopping
			shopping = float(raw_input("Shopping Budget: "))
			my_month.set_budget_values('Shopping', shopping)
	
		elif user_choice == "7":    #ADD Personal
			personal = float(raw_input("Personal Budget: "))
			my_month.set_budget_values('Personal', personal)
		
		elif user_choice == "8":    #ADD Health & Fitness
			health_fitness = float(raw_input("Health & Fitness Budget: "))
			my_month.set_budget_values('Health & Fitness', health_fitness)
		
		elif user_choice == "9":    #ADD Entertainment
			entertainment = float(raw_input("Entertainment Budget: "))
			my_month.set_budget_values('Entertainment', entertainment)
		
		elif user_choice == "10":   #ADD Travel
			travel = float(raw_input("Travel Budget: "))
			my_month.set_budget_values('Travel', travel)
	
		elif user_choice == "11":   #ADD Medical
			medical = float(raw_input("Medical Budget: "))
			my_month.set_budget_values('Medical', medical)
		
		elif user_choice == "12":   #ADD Savings
			savings = float(raw_input("Savings Budget: "))
			my_month.set_budget_values('Savings', savings)
		
		elif user_choice not in ("1" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"):
				print "Woops! Please choose a category by selecting it's cooresponding number." 

	my_month_budget_data.append(my_month.budget) #CREATING LIST OF BUDGET DATA


def return_unallocated_money_question(): 
	my_month_unallocated_money = float(my_month.calculate_unallocated_money(my_month_income, my_month.calculate_total_est_spending()))
	if my_month_unallocated_money > 0:
		user_choice = raw_input("Based on your monthly income of $%.2f and your total estimated budget of $%.2f, you have $%.2f remaining, would you like to allocate it into budget category? (Y/N) " % (
						my_month_income, 
						my_month.calculate_total_est_spending(), 
						my_month_unallocated_money
						))
		if (str.upper(user_choice) == "Y"):  #user wants to add extra money to category 
			edit_budget()         
		else:
			None
	if my_month_unallocated_money < 0:
		user_choice = raw_input("Your budget of $%.2f is net negative comparatively with your income of $%.2f.  Would you like to edit your exisitng budget? (Y/N) " % (
						my_month.calculate_total_est_spending(),
						my_month_income
						))
		if (str.upper(user_choice) == "Y"):  #user wants to add extra money to category 
			edit_budget() 
		else:
			None  




####  CREATE BUDGET #####

# "1. Create New Budget",
# "2. Create Budget from Previous Month's Expenditures",
# "3. Use a Budget from a Previous Month",
# "4. Return to Home"


def option_create_new_budget():
	month = raw_input("Current Month: ")
	#month = "3"
	year = raw_input("Current Year: ")
	#year = "2016"
	my_month = Month(month, year) 
	
	my_month_budget_data = []


	print "Your current budget for %s is:" % (month)  
	my_month.return_current_budget(my_month_budget_data)  #prints out entire budget w/ "$0.00" next to each category 
	# my_month.return_current_budget(my_month.budget)



	print "\n" 
	my_month.set_all_budget_values(my_month_budget_data)  #user inputs all values for each category 
	# my_month.set_all_budget_values(my_month.budget)
	
	my_month.income = float(raw_input("This month's income: "))
	#my_month.income = 1275.80

	my_month_income = my_month.income  					  #creating variable my_month_income
	
	my_month.return_current_budget(my_month_budget_data)  #prints budget w/ new values 

	return_unallocated_money_question()


############



#####  CREATE BUDGET #####

# "1. Create New Budget",
# "2. Create Budget from Previous Month's Expenditures",
# "3. Use a Budget from a Previous Month",
# "4. Return to Home"

def option_create_budget():  #OPTION 1: Create Budget
	menu = (
		"1. Create New Budget",
		"2. Create Budget from Previous Month's Expenditures",
		"3. Use a Budget from a Previous Month",
		"4. Return to Home"
		)
	for choice in menu:
		print "\t" + choice 
	user_choice = raw_input("Choose desired action by selecting it's corresponding number: ")
	
	if (user_choice == "4") or (str.upper(user_choice) == "HOME"):  #option 4: return home
		None
	
	elif user_choice == "1":      #option 1: Create New Budget
		option_create_new_budget()  #FUNCTION FROM USER_GUIDED_MENU_DETAIL

	elif user_choice == "2":      #option 2: Create Budget from Previous Month's Expenditures
		print "TO DO: Create Budget from Previous Month's Expenditures"
	
	elif user_choice == "3":      #option 3: Use a Budget from a Previous Month
		print "TO DO: Use a Budget from a Previous Month"
	
	elif  user_choice not in ("1" , "2", "3", "4"):
		print "\n" + "Woops! Please choose which action by selecting it's cooresponding number." + "\n" 






#####  VIEW CURRENT BUDGET #####
# "1. Edit Above Budget",
# "2. Return to Home"

def option_view_current_budget():  #OPTION 2:  View This Month's Budget
	print "Your current budget for this month is:"  #THIS MONTH (CALL CLASS MARCH W/ DATA OF DATE using %s - have it put the current month you are creating data for)
	my_month.return_current_budget(my_month_budget_data)  #prints budget w/ new values 
	menu = (
		"1. Edit Above Budget",
		"2. Return to Home"
		)
	for choice in menu:
		print "\t" + choice
	user_choice = raw_input("Choose desired action by selecting it's corresponding number: ")
	
	if (user_choice == "2") or (str.upper(user_choice) == "HOME"):    #option 2: return home
		None
	
	elif user_choice == "1":  	 #option 1: Edit Above Budget
		edit_budget_by_cateogry()  #FUNCTION FROM USER_GUIDED_MENU_DETAIL
	
	elif user_choice not in ("1" , "2"):
		print "Woops! Please choose which action by selecting it's cooresponding number." 







#####  ADD TRANSACTION #####
# "1. Add Transaction to Category",
# "2. Return to Home"

def option_add_transaction():  #OPTION 3:  Add Transactions for This Month
	expenditure_items = (
			"1. Rent", 
			"2. Utilities",
			"3. Transportation",
			"4. Food & Dining", 
			"5. Bars", 
			"6. Shopping", 
			"7. Personal", 
			"8. Health & Fitness",
			"9. Entertainment",
			"10. Travel",
			"11. Medical",
			"12. Savings",
			"13. Return to home"
			)
	while (True): 
		for category in expenditure_items:
			print "\t" + category
		user_choice = raw_input("Choose which category you would like to add a transaction to by selecting it's corresponding number: ")
	
		if (user_choice == "13") or (str.upper(user_choice) == "HOME"):  #option 15: return home
			None
	
		elif user_choice == "1":    #ADD transaction to Rent
			rent = float(raw_input("Add to Rent: "))
			my_month.add_transaction('Rent', rent)

		elif user_choice == "2":    #ADD transaction to Utilities
			utilities = float(raw_input("Add to Utilities: "))
			my_month.add_transaction('Utilities', utilities)
	
		elif user_choice == "3":    #ADD transaction to Transportation
			transportation = float(raw_input("Add to Transportation: "))
			my_month.add_transaction('Transportation', transportation)
	
		elif user_choice == "4":    #ADD transaction to Food & Dining
			food_dining = float(raw_input("Add to Food & Dining: "))
			my_month.add_transaction('Food & Dining', food_dining)
	
		elif user_choice == "5":    #ADD transaction to Bars
			bars = float(raw_input("Add to Bars: "))
			my_month.add_transaction('Bars', bars)
	
		elif user_choice == "6":    #ADD transaction to Shopping
			shopping = float(raw_input("Add to Shopping: "))
			my_month.add_transaction('Shopping', shopping)
	
		elif user_choice == "7":    #ADD transaction to Personal
			personal = float(raw_input("Add to Personal: "))
			my_month.add_transaction('Personal', personal)
		
		elif user_choice == "8":    #ADD transaction to Health & Fitness
			health_fitness = float(raw_input("Add to Health & Fitness: "))
			mmy_month.add_transaction('Health & Fitness', health_fitness)
		
		elif user_choice == "9":    #ADD transaction to Entertainment
			entertainment = float(raw_input("Add to Entertainment: "))
			my_month.add_transaction('Entertainment', entertainment)
		
		elif user_choice == "10":   #ADD transaction to Travel
			travel = float(raw_input("Add to Travel: "))
			my_month.add_transaction('Travel', travel)
	
		elif user_choice == "11":   #ADD transaction to Medical
			medical = float(raw_input("Add to Medical: "))
			my_month.add_transaction('Medical', medical)
		
		elif user_choice == "12":   #ADD transaction to Savings
			savings = float(raw_input("Add to Savings: "))
			my_month.add_transaction('Savings', savings)
		
		elif user_choice not in ("1" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"):
				print "Woops! Please choose a category by selecting it's cooresponding number." 

	my_month_expenditure_data.append(my_month.expenditures) #CREATING LIST OF BUDGET DATA
	
	my_month.calculate_budget_spending_tracker_value(my_month_budget_data, my_month_expenditure_data)  #calculating spending tracker valus
	my_month_budget_spending_tracker_data.append(my_month.budget_spending_tracker)  #saving budget vs. spending tracker data





#####  ADD VIEW SPENDING BUDGET TRACKER #####
# lists out budget-goal-tracker 
		# (e.g. utilities_budget = $160 | utilities_expenditure = $111 | budget_goal_tracker = $49) 
		# category: $$ spent so far on that category
#"1. Add Transaction",
#"2. View A Different Month's Spending Patterns", 
#"3. Return to Home"


def option_track_budget_spending_goals():  #OPTION 4:  Track This Month's Spending Goals
	my_month.return_current_budget_spending_tracker(my_month_budget_spending_tracker_data)  #prints all budget goals vs. spending data 

	menu = (
		"1. Add Transaction",
		"2. View A Different Month's Spending Patterns", 
		"3. Return to Home"
		)
	for choice in menu:
		print "\t" + choice
	user_choice = raw_input("Choose desired action by selecting it's corresponding number:: ")
	if (user_choice == "3") or (str.upper(user_choice) == "HOME"):  
		None
	
	elif user_choice == "1":   #option 1: Add Transaction
		option_add_transaction()
	
	elif user_choice == "2":   #option 2: View A Different Month's Spending Patterns
		print "TO DO: View A Different Month's Spending Patterns"
	
	elif  user_choice not in ("1" , "2", "3"):
		print "Woops! Please choose which action by selecting it's cooresponding number." 




def file_save():  #CURRENT ONLY SAVES FOR 1 MONTH - DATA WILL OVERWRITE  (use a file name as a parmameter?)
	with open("my_month_output_data.csv", "w") as my_month_out_file:
		fieldnames = [
				'month', 
				'year', 
				'income', 
				'budget', 
				'expenditures', 
				'budget_spending_tracker'
				]
		writer = csv.DictWriter(my_month_out_file, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow(
						{
						'month' : 'March',    #HOW TO INPUT THIS - CALLING %S OF CLASS OBJECT "MONTH"
						'year' : 2016, 		  #HOW TO INPUT THIS - CALLING %S OF CLASS OBJECT "MONTH"
						'income' : my_month_income, 
						'budget' : my_month_budget_data, 
						'expenditures' : my_month_expenditure_data, 
						'budget_spending_tracker' : my_month_budget_spending_tracker_data
						}
						)


def convert_list_to_dict(list):
	new_dict = {}
	i = 0
	for item in list:
		new_dict[list[i].split(':')[0]] = list[i].split(':')[1]
		i += 1
	return new_dict



def file_open():
	with open("my_month_output_data.csv", "r") as my_month_in_file:
		reader = csv.reader(my_month_in_file)
		extract_month = []
		extract_year = []
		extract_income = []
		extract_budget = []
		extract_expenditures = []
		extract_budget_spending_tracker = []
		for row in reader:
			extract_month = row[0]
			extract_year = row[1]
			extract_income = row[2]
			extract_budget = row[3]
			extract_expenditures = row[4]
			extract_budget_spending_tracker = row[5]
	  

	extract_budget_list = (extract_budget[2:-2]).split(", ")
	extract_budget_dict = convert_list_to_dict(extract_budget_list)

	extract_expenditures_list = (extract_expenditures[2:-2]).split(", ")
	extract_expenditures_dict = convert_list_to_dict(extract_expenditures_list)


	extract_budget_spending_tracker_list = (extract_budget_spending_tracker[2:-2]).split(", ")
	extract_budget_spending_tracker_dict = convert_list_to_dict(extract_budget_spending_tracker_list)





