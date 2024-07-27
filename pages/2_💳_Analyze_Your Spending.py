# import necessary packages
import pandas as pd
import streamlit as st

# import functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_spending import setup_data, monthly_net_gain, visualize_spending, analyze_income

### add title on main page
st.title("Your Finances At A Glance")

### allow user to upload their transactions to try demo in sidebar
file = st.sidebar.file_uploader(label="Upload your transactions or demo using the example file", type=["csv", "xlsx"]) # upload file
yes_demo = st.sidebar.button("Example file") # try demo

# if the user has uploaded their file, create dashboard using that file:
if file is not None:
	## read in as a dataframe
	transactions = setup_data(file)

	## create and show bar plots showing the monthly income and expenses and net gain
	net_gain = monthly_net_gain(transactions)
	## create and show pie charts describing the types of income and categories spent on
	col1, col2 = st.columns(2)
	spending = visualize_spending(transactions, col1)
	income = analyze_income(transactions, col2)
	

# or use example file to create dashbaord
elif yes_demo: 
	## use sample transactions file from GitHub
	url = "https://github.com/kthuang20/finance-app/raw/main/sample_data/transactions_2024_07_27.csv"
	## read in as a dataframe
	transactions = setup_data(url)

	## create and show bar plots showing the monthly income and expenses and net gain
	net_gain = monthly_net_gain(transactions)
	## create and show pie charts describing the types of income and categories spent on
	col1, col2 = st.columns(2)
	spending = visualize_spending(transactions, col1)
	income = analyze_income(transactions, col2)
	