### import necessary packages
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

### function to set up the data
def setup_data(file):
	## read the file as a dataframe
	transactions = pd.read_csv(file)

	## remove transfers
	transactions = transactions[transactions["Category"] != "Transfers"]

	## create three new columns for the date column: year, month, day
	transactions["Date"] = pd.to_datetime(transactions["Date"])
	transactions['Year'] = transactions['Date'].dt.year
	transactions['Month'] = transactions['Date'].dt.month
	transactions['Day'] = transactions['Date'].dt.day

	## convert the amount into numerical values
	transactions["Amount (in $)"] = transactions["Amount (in $)"].astype(float)
	## make sure that expenses are negative values
	expenses = transactions.loc[transactions["Transaction Type"] == "Expense", "Amount (in $)"]
	transactions.loc[transactions["Transaction Type"] == "Expense", "Amount (in $)"] = expenses.abs() * -1

	return transactions

### function to generate bar plot tracking expenses and income over time
def monthly_net_gain(transactions):
	## calculate monthly income
	income = transactions.loc[transactions["Amount (in $)"] > 0, ["Month", "Year", "Amount (in $)"]]
	monthly_income = income.groupby(["Year", "Month"]).sum()

	## calculate monthly expenses
	expenses = transactions.loc[transactions["Amount (in $)"] < 0, ["Month", "Year", "Amount (in $)"]]
	monthly_expenses = expenses.groupby(["Year", "Month"]).sum().abs()

	## create a dataframe summarizing the monthly income and expenses
	net_gain = pd.merge(monthly_income, monthly_expenses, on=["Year", "Month"], how="outer").reset_index()
	net_gain.columns = ["Year", "Month", "Total Income", "Total Expenses"]
	net_gain.fillna(0, inplace=True)

	## add a column with the name of the month
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
	net_gain["Month Name"] = net_gain["Month"].map(month_names)

	## include a column describing the net gain
	net_gain["Net Gain"] = net_gain["Total Income"] - net_gain["Total Expenses"]


	## create a bar plot showing the monthly income and expenses
	fig1 = px.bar(net_gain, x="Month Name", y=["Total Income", "Total Expenses"],
				 title = "Monthly Income and Expenses",
				 labels={"Month Name": "Month", "value": "Amount", "variable": "Type"})
	fig1.update_layout(yaxis_title = "Amount (in $)")

	## create line plot tracking the net gain
	fig2 = px.bar(net_gain, x="Month Name", y="Net Gain",
				   title = "Net Gain",
				   labels={"Month Name": "Month"})

	## create a container separated by tabs to show results to user
	tab1, tab2 = st.tabs(["Monthly Income and Expenses", "Net Gain"])
	## show monthly income and expense in the first tab and the line plot describing net gain on the second tab
	tab1.plotly_chart(fig1)
	tab2.plotly_chart(fig2)

	return net_gain

### function to generate a pie chart describing how much was spent in various spending categories
def visualize_spending(transactions, col):
	## select the data describing income
	spending = transactions[transactions["Transaction Type"] == "Expense"]
	spending["Amount (in $)"] = spending["Amount (in $)"].abs()

	## create a pie chart describing how much of each type income the user 
	fig = px.pie(spending, values="Amount (in $)", names="Subcategory", title="Spending Categories")
	col.plotly_chart(fig)

	return spending

### function to generate composition of income
def analyze_income(transactions, col):
	## select the data describing income
	income = transactions[transactions["Category"] == "Income"]

	## create a pie chart describing how much of each type income the user 
	fig = px.pie(income, values="Amount (in $)", names="Subcategory", title="Types of Income Earned")
	col.plotly_chart(fig)
	return income

### function to show summary statistics
def sum_stats(transactions, net_gain, spending, income):
	## add section title
	st.header("Summary Statistics")

	## calculate total saved
	total_earned = net_gain["Total Income"].sum()
	total_spent = net_gain["Total Expenses"].sum()
	total_saved = total_earned - total_spent
	percent_earned = total_saved/total_earned * 100
	## calculate how much you earned and spent on average
	avg_amt_earned = net_gain["Total Income"].mean()
	avg_amt_spent = net_gain["Total Expenses"].mean()

	## calculate the average % expenses (excluding months where you spent more than you earned)
	net_gain["% spent"] = net_gain["Total Expenses"]/net_gain["Total Income"] * 100
	avg_percent_spent = net_gain.loc[np.isfinite(net_gain["% spent"]), "% spent"].mean()

	## store the greatest source of spending and income
	income_by_source = income.groupby("Subcategory")["Amount (in $)"].sum().reset_index()
	top_income_source = income_by_source.sort_values("Amount (in $)", ascending=False).iloc[0, 0]

	spending_by_cat = spending.groupby("Subcategory")["Amount (in $)"].sum().reset_index()
	top_spending_cat = spending_by_cat.sort_values("Amount (in $)", ascending=False).iloc[0, 0]

	## create a section with 2 columns
	col1, col2 = st.columns(2)
	## show all results from net gain on the left column
	col1.write("On average, you:")
	col1.write(f"* Earned ${avg_amt_earned:,.2f}/month")
	col1.write(f"* Earned ${avg_amt_spent:,.2f}/month")
	col1.write(f"* Spent {avg_percent_spent:.2f}% of your income per month")
	## show all specifics from spending and income on the right
	col2.write("You: ")
	col2.write(f"* Earned a total of: ${total_earned:,.2f}, most of which was from {top_income_source.lower()}")
	col2.write(f"* Spent a total of: ${total_spent:,.2f}, most of which was from {top_spending_cat.lower()}")
	col2.write(f"* Saved a total of: ${total_saved:,.2f}, which was {percent_earned:.2f}% of what you earned!")

	
