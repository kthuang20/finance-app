### import necessary packages
import pandas as pd
import streamlit as st
import plotly.express as px
import plost

### import self written functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_spending import setup_data as setup_spending
from analyze_investments import setup_data as setup_investments

### function to set up both files
def setup_data(spending_file, investments_file):
	## setup up the spending file
	spending_transactions = setup_spending(spending_file)
	## create a dataframe with the 
	expenses = spending_transactions[spending_transactions["Transaction Type"] == "Expense"]
	## convert expenses to positive values
	expenses["Amount (in $)"] = expenses["Amount (in $)"].abs()
	## remove unrelevant columns
	cols2keep = ["Month","Amount (in $)"]
	expenses = expenses[cols2keep]
	## create a dataframe with the monthly expenses
	monthly_expenses = expenses.groupby("Month")["Amount (in $)"].sum().reset_index()

	## create a dataframe containing your interest earned from savings accounts
	interest_income = spending_transactions[spending_transactions["Subcategory"] == "Interest income"]
	## keep only date columns and amount earned
	interest_income = interest_income[cols2keep]
	## create a dataframe with the total interest earned monthly
	monthly_interest = interest_income.groupby("Month")["Amount (in $)"].sum().reset_index()
	## add a column to label that these amounts are for investment income
	monthly_interest["Type"] = "Investment Income"
	monthly_interest["Category"] = "Interest Income"

	## setup the investments data
	investments, dividends = setup_investments(investments_file)
	## remove unrelevant columns in dividends dataframe
	cols2keep = ["Month", "Amount"]
	investments = investments[cols2keep]
	investments.rename(columns={"Amount": "Amount (in $)"}, inplace=True)
	## create a dataframe containing the monthly investments earned per month
	monthly_investments = investments.groupby("Month")["Amount (in $)"].sum().reset_index()
	## replace amounts with 4% * investments added
	monthly_investments["Amount (in $)"] = monthly_investments["Amount (in $)"] * 0.04
	## add a column labelling it as investment income and what type of investment income
	monthly_investments["Type"] = "Investment Income"
	monthly_investments["Category"] = "4% Income"

	## remove unrelevant columns in dividends dataframe
	dividends = dividends[cols2keep]
	dividends.rename(columns={"Amount": "Amount (in $)"}, inplace=True)
	## create a dataframe containing the total dividends earned per month
	monthly_dividends = dividends.groupby("Month")["Amount (in $)"].sum().reset_index()
	## add a column to label that these amounts are for investment income
	monthly_dividends["Type"] = "Investment Income"
	monthly_dividends["Category"] = "Dividend Income"
	

	### combine the investment income dataframes into one
	investment_income = pd.concat([monthly_interest, monthly_investments])
	investment_income = pd.concat([investment_income, monthly_dividends])
	## create a dataframe containing the monthly investments earned per month
	monthly_investments = investment_income.groupby("Month")["Amount (in $)"].sum().reset_index()

	return monthly_expenses, monthly_investments


### function to create a line plot tracking the monthly investments and expenses
def show_crossover(monthly_expenses, monthly_investments):
	## combine monthly investments and expenses into one dataframe
	monthly_expenses["Type"] = "Monthly Expenses"
	monthly_investments["Type"] = "Investment Income"
	crossover_data = pd.concat([monthly_expenses, monthly_investments])

	## create a line plot comparing monthly investments and expenses
	fig = px.line(crossover_data,
				  x = "Month",
				  y = "Amount (in $)",
				  color = "Type",
				  markers = True)
	## show line plot
	st.plotly_chart(fig)

	return crossover_data

### function to generate summary, describing the user reached crosspoint during any month
def gen_sum(monthly_expenses, monthly_investments):
	## combine the two dataframes horizontally so amounts are side by side
	all_data = pd.merge(monthly_expenses.drop("Type", axis=1), monthly_investments.drop("Type", axis=1), 
						on="Month", how="outer", suffixes=("_expenses", "_investments"))
	## fill NAs with 0
	all_data.fillna(0, inplace=True)

	## add a column with name of the month
	month_names = {1: "January",
				   2: "February",
				   3: "March",
				   4: "April",
				   5: "May",
				   6: "June",
				   7: "July",
				   8: "August",
				   9: "September",
				   10: "October",
				   11: "November",
				   12: "December"}
	all_data["Month Name"] = all_data["Month"].map(month_names)

	## add a column stating whether they've reached crosspoint for each month
	all_data["crosspoint"] = all_data["Amount (in $)_investments"] >= all_data["Amount (in $)_expenses"] 
	## store the months that the user reached the crosspoint
	crosspoint_months = all_data.loc[all_data["crosspoint"], "Month Name"].tolist()

	## explain to user how the graph was generated
	st.markdown('''
		#### *How monthly expenses and investments were calculated*
		Monthly expenses were calculated by taking the sum of all the expenses made that month.
		The monthly investment income was determined by summing the following components:
		1. Interest earned from high yield savings accounts that month
		2. 4% of all investments added that month (assuming 4% rule)
		3. Dividends earned from investments that month
		''')

	## explain results to user
	st.write("#### *Results*")
	if crosspoint_months:
		if len(crosspoint_months) >= 3:
			months = ", ".join(crosspoint_months)
		elif len(crosspoint_months) == 2:
			months = f"{crosspoint_months[0]} and {crosspoint_months[1]}"
		else: 
			months = crosspoint_months[0]
		st.write(f"Based on the calculations made above, you reached the crosspoint in the following months: \
			{months}. Congratulations!!!!")

	else:
		st.write("Based on the calculations made above, you did not reach the crossover point at any point.")
