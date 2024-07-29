# import necessary packages
import pandas as pd
import streamlit as st

# import functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_investments import setup_data

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

# if the user has uploaded their file, create dashboard using that file:
if file is not None:
	## read in as a dataframe
	transactions = setup_data(file)
	

# or use example file to create dashbaord
elif yes_demo: 
	## use sample transactions file from GitHub
	url = "https://github.com/kthuang20/finance-app/raw/main/sample_data/transactions_2024_07_27.csv"
	## read in as a dataframe
	transactions = setup_data(url)

	