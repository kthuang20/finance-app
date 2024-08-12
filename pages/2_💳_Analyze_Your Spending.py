### import necessary packages
import pandas as pd
import streamlit as st

### import functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_spending import setup_data, monthly_net_gain, visualize_spending, analyze_income, sum_stats

### configure settings of page
st.set_page_config(
	layout = "wide",
	initial_sidebar_state = "expanded")

### add title on main page
st.title("Your Finances At A Glance")
st.sidebar.markdown("***Note:*** This analysis only works with .csv files that are formatted like the \
[example file](https://github.com/kthuang20/finance-app/raw/main/sample_data/spending_transactions.csv).")

### allow user to upload their transactions to try demo in sidebar
file = st.sidebar.file_uploader(label="Upload your spending transactions:", type=".csv") # upload file
try_demo = st.sidebar.button("Example")

### add credits to sidebar
st.sidebar.markdown('''
	---
	*Created by [Katie Huang](https://kthuang20.github.io/Katie_Portfolio/about/)*''')

### function to create dashboard
def create_dashboard(file):
	## setup the data
	transactions = setup_data(file)
	## create and show bar plots showing the monthly income and expenses and net gain
	net_gain = monthly_net_gain(transactions)
	## create a section with two columns
	col1, col2 = st.columns(2)
	## show a pie chart describing spending categories on the left column
	spending = visualize_spending(transactions, col1)
	## show a pie chart describing sources of income on the right column
	income = analyze_income(transactions, col2)
	## add summary statistics
	sum_stats(transactions, net_gain, spending, income)

### if the user has uploaded their file, create dashboard using that file:
if file is not None:
	## show contents of dashboard
	create_dashboard(file)

### or use example file to create dashbaord
elif try_demo: 
	## use sample transactions file from GitHub
	url = "https://github.com/kthuang20/finance-app/raw/main/sample_data/spending_transactions.csv"
	## show contents of dashboard
	create_dashboard(url)
	