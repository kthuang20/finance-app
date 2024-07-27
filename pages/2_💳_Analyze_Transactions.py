# import necessary packages
import pandas as pd
import streamlit as st


### create a multiple pages
st.set_page_config(
	page_title="Finance App",
	page_icon="💰"
	)

### add title on main page
st.title("Finance App")
'''This finance app takes in your yearly transactions to help you understand how much you saved and spent.'''


### allow user to upload their transactions to try demo in sidebar
file = st.sidebar.file_uploader(label="Upload your transactions or demo using the example file", type=["csv", "xlsx"]) # upload file
yes_demo = st.sidebar.button("Example file") # try demo

# if the user has uploaded their file, create dashboard using that file:
if file is not None:
	## read in as a dataframe
	transactions = run_analysis.setup_data(file)
	st.write(transactions.head())

# or use example file to create dashbaord
if yes_demo: 
	## use sample transactions file from github
	url = "https://github.com/kthuang20/finance-app/raw/main/data/transactions_2024_07_27.csv"
	transactions = run_analysis.setup_data(url)
	st.write(transactions.head())