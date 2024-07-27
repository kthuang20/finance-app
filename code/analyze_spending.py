import pandas as pd
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
	transactions["Amount (in $)"] = pd.to_numeric(transactions["Amount (in $)"])
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

	## convert numerical months to their name of the month
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
	net_gain["Month Names"] = net_gain["Month"].map(month_names)

	## include a column describing the net gain
	net_gain["Net Gain"] = net_gain["Total Income"] - net_gain["Total Expenses"]


	## create a bar plot showing the monthly income and expenses
	fig1 = px.bar(net_gain, x="Month Names", y=["Total Income", "Total Expenses"],
				 title = "Monthly Income and Expenses",
				 labels={"Month Names": "Month", "value": "Amount", "variable": "Type"})
	fig1.update_layout(yaxis_title = "Amount (in $)")

	## create line plot tracking the net gain
	fig2 = px.bar(net_gain, x="Month Names", y="Net Gain",
				   title = "Net Gain",
				   labels={"Month Names": "Month"})

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
	income = transactions[transactions["Transaction Type"] == "Income"]

	## create a pie chart describing how much of each type income the user 
	fig = px.pie(income, values="Amount (in $)", names="Subcategory", title="Types of Income Earned")
	col.plotly_chart(fig)
	return income
