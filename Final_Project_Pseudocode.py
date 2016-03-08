#pseudocode

#CA$H TRACKS PROGRAM

############
#MENU - USER GUIDE:

# 1. create budget
	# A. create new budget
	# B. create budget from previous month's expenditures
	# C. use last month's budget 
	# D. return to main menu 


# 2. view this month's budget
	# (prints full budget)
	# A. edit above budget
	# B. return to main menu



# 3. add transactions
	# A. select one of the following categories to add a transaction to
	# (print each category w/ a number associated to it)
	# (shows budget-goal-tracker --> budget_category_value - expenditure_value)
	# B. return to main menu


# 4. track this month's budget spending goals
	# lists out budget-goal-tracker 
		# (e.g. utilities_budget = $160 | utilities_expenditure = $111 | budget_goal_tracker = $49) 
		# category: $$ spent so far on that category
	# option to return to main menu


########

# PROGRAM:

# March = object

# e.g. MARCH DATA

# have raw_inputs to go through menu to add in data
	#march_budget --> create dictionary 
	#march_expenditures --> create dictionary 


	#save march_budget_data as json file
	#save march_expenditure_data as json file


#SAVE AS JSON CONVERSION


#######

# Class: Month (year, month)
	# attributes:
		# year
		# month
		# income
		# budget
		# expenditures

# methods:
		# set budget value
		# set budget values (add all)
		# add transaction to expense category
		# display $$ spent within each budget_category based on designated budget_value (budget_goal_tracker)
		# calcualte total estimated expenses (add amts of budget values)
		# calculate unallocated $$
		# return current budget:
			# budget_category : budget_value
		# return current expenditures:  --> how much user has spent so far within each category
			# budget_category : current_total_transactions


#########




