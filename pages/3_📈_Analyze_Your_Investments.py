### import necessary packages
import pandas as pd
import streamlit as st

### import functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_investments import setup_data, show_monthly_investments, show_investment_types, show_dividends

### configure settings of page
st.set_page_config(
	layout = "wide",
	initial_sidebar_state = "expanded")

### add title on main page
st.title("Your Investments At A Glance")
st.sidebar.markdown("***Note:*** This app only works with .csv and .xlsx files that are formatted like the \
[example file](https://github.com/kthuang20/finance-app/raw/main/sample_data/InvestmentTransactions.csv)")

### allow user to upload their transactions to try demo in sidebar
file = st.sidebar.file_uploader(label="Upload your transactions or demo using the example file", type=["csv", "xlsx"]) # upload file
yes_demo = st.sidebar.button("Example file") # try demo

### add name to sidebar
st.sidebar.markdown('''
	--- 
	*Created by [Katie Huang](https://kthuang20.github.io/Katie_Portfolio/)*''')

### function to create dashboard
def create_dashboard(investments, dividends):
	## generate bar plots showing the investments made each month
	show_monthly_investments(investments) 
	## create two columns
	col1, col2 = st.columns(2)
	## generate a pie chart showing the types of investments made on left column
	show_investment_types(investments, col1)
	## generate a pie chart showing the dividends earned made on right column
	show_dividends(dividends, col2)

### if the user has uploaded their file, create dashboard using that file:
if file is not None:
	## read in as a dataframe
	investments, dividends = setup_data(file)
	## create dashboard
	create_dashboard(investments, dividends)

### or use example file to create dashbaord
elif yes_demo: 
	## use sample transactions file from GitHub
	url = "https://github.com/kthuang20/finance-app/raw/main/sample_data/InvestmentTransactions.csv"
	## read in as a dataframe
	investments, dividends = setup_data(url)
	## create dashboard
	create_dashboard(investments, dividends)
	