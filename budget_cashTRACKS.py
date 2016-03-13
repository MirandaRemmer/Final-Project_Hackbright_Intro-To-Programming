#budget listing class


class Month(object):
	def __init__(self, month, year):
		self.month = month
		self.year = year
		self.income = ""
		self.budget = {						#monthly budget
					'Rent' : 0.00,
					'Utilities' : 0.00,
					'Transportation' : 0.00,
					'Food & Dining' : 0.00,
					'Bars' : 0.00,
					'Shopping' : 0.00,
					'Personal' : 0.00,
					'Health & Fitness' : 0.00,
					'Entertainment' : 0.00,
					'Travel' : 0.00,
					'Medical' : 0.00,
					'Savings' :0.00
					}
		self.expenditures = {    				#monthly expenditures [items you spend money on]
					'Rent' : 0.00,
					'Utilities' : 0.00,
					'Transportation' : 0.00,
					'Food & Dining' : 0.00,
					'Bars' : 0.00,
					'Shopping' : 0.00,
					'Personal' : 0.00,
					'Health & Fitness' : 0.00,
					'Entertainment' : 0.00,
					'Travel' : 0.00,
					'Medical' : 0.00,
					'Savings' :0.00
					}
		self.budget_spending_tracker = {      #keeps track of budget - expenditure for each category item
					'Rent' : 0.00,
					'Utilities' : 0.00,
					'Transportation' : 0.00,
					'Food & Dining' : 0.00,
					'Bars' : 0.00,
					'Shopping' : 0.00,
					'Personal' : 0.00,
					'Health & Fitness' : 0.00,
					'Entertainment' : 0.00,
					'Travel' : 0.00,
					'Medical' : 0.00,
					'Savings' :0.00
					}
		self.dict_order = [
				'Rent', 
				'Utilities',
				'Transportation',
				'Food & Dining', 
				'Bars', 
				'Shopping', 
				'Personal', 
				'Health & Fitness',
				'Entertainment',
				'Travel',
				'Medical',
				'Savings'
				]


	def set_budget_value(self, budget_category, budget_category_value):  #set values to budget category 
		self.budget[budget_category] = float(budget_category_value)
	
	def set_budget_values(self, budget_category_dict):
		self.budget = budget_category_dict

	def set_all_budget_values(self, budget_category):
		for budget_category in self.dict_order:
			self.budget[budget_category] = float(raw_input("%s Budget: " % (budget_category)))

	def add_transaction(self, expenditure_category, transaction_amt):  #add transactions to track monthly spending
		self.expenditures[expenditure_category] = self.expenditures[expenditure_category] + transaction_amt

	# def set_budget_spending_tracker_value(self, budget_value, expenditure_value):
	# 	remaining_spending_allowance_per_category = float(self.budget[budget_value.sort()]) - float(self.expenditures[expenditure_value.sort()]) #shows how much $ is left to spend in budget category
	# 	self.budget_spending_tracker[category] = float(remaining_spending_allowance_per_category)

	# def calculate_budget_spending_tracker_value(self, category):
	# 	index = 0 
	# 	for index in range(len(self.budget_spending_tracker)):
	# 		if self.budget[index] == self.expenditures[index]:
	# 		self.budget_spending_tracker[index] = float((self.budget[index] - self.expenditures[index]))
	# 	index +=1

	def calculate_budget_spending_tracker_value(self, budget_dict, expenditure_dict):  #removed category 
		for key in self.budget.viewkeys() and self.expenditures.viewkeys():
			self.budget_spending_tracker[key] = float(self.budget[key] - self.expenditures[key])
		return self.budget_spending_tracker


		# self.budget_spending_tracker['Rent'] = float(self.budget['Rent'] - self.expenditures['Rent'])
		
		# if category in self.budget == category in self.expenditures:
		# 	self.budget_spending_tracker[category] = float((self.budget[category] - self.expenditures[category]))


	# def calculate_all_category_spending_allowances(self, budget_category_dict, expenditure_category_dict):
	# 	for self.budget[budget_category] in self.expenditures[expenditure_category]:
	# 		return float(self.budget[budget_category]) - float(self.expenditures[expenditure_category])
	

	def calculate_total_est_spending(self): #add all budget values to calculate expected sepending / estimate that months spending (#calculate_total_budget_allocation)
		budget_added = float(
					self.budget['Rent'] +
					self.budget['Utilities'] +
					self.budget['Transportation'] +
					self.budget['Food & Dining'] +
					self.budget['Bars'] +
					self.budget['Shopping'] +
					self.budget['Personal'] +
					self.budget['Health & Fitness'] +
					self.budget['Entertainment'] +
					self.budget['Travel'] +
					self.budget['Medical'] +
					self.budget['Savings']
					)
		return budget_added
	

	def calculate_unallocated_money(self, income, budget_added):
		unallocated_money = float(self.income - budget_added)
		return unallocated_money


	def return_current_budget(self, budget_dictionary):
		for i in self.dict_order:
			print i + ":", "$" + "%0.2f" % self.budget[i]


	def return_current_expenditures(self, expenditure_dictionary):
		for i in self.dict_order:
			print i + ":", "$" + "%0.2f" % self.expenditures[i]


	def return_current_budget_spending_tracker(self, budget_spending_tracker_dict):
		for i in self.dict_order:
			print i + ":", "$" + "%0.2f remaining in %s budget" % (self.budget_spending_tracker[i], i.lower())





	#MAKE SAVING A FILE A FUNCTION??






	



			
		




	










