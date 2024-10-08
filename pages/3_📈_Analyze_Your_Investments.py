### import necessary packages
import pandas as pd
import streamlit as st

### import self written functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_investments import setup_data, show_monthly_investments, show_investment_types, show_dividends, sum_stats

### configure settings of page
st.set_page_config(
	layout = "wide",
	initial_sidebar_state = "expanded")

### add title on main page
st.title("Your Investments At A Glance")
st.sidebar.markdown("***Note:*** This analysis only works with .csv files that are formatted like the \
[example file](https://github.com/kthuang20/finance-app/raw/main/sample_data/InvestmentTransactions.csv)")

### allow user to upload their transactions to try demo in sidebar
file = st.sidebar.file_uploader(label="Upload your investment transactions:", type=".csv") # upload file
try_demo = st.sidebar.button("Example") # try demo

### add credits to sidebar
st.sidebar.markdown('''
	--- 
	*Created by [Katie Huang](https://kthuang20.github.io/Katie_Portfolio/about/)*''')

### function to create dashboard
def create_dashboard(file):
	## setup the data
	investments, dividends = setup_data(file)
	## generate bar plots showing the investments made each month
	show_monthly_investments(investments) 
	## create two columns
	col1, col2 = st.columns(2)
	## generate a pie chart showing the types of investments made on left column
	show_investment_types(investments, col1)
	## generate a pie chart showing the dividends earned made on right column
	show_dividends(dividends, col2)
	## generate summary statistics
	sum_stats(investments, dividends)

### if the user has uploaded their file, create dashboard using that file:
if file is not None:
	## create dashboard
	create_dashboard(file)

### or use example file to create dashbaord
elif try_demo: 
	## use sample transactions file from GitHub
	url = "https://github.com/kthuang20/finance-app/raw/main/sample_data/InvestmentTransactions.csv"
	## create dashboard
	create_dashboard(url)
	