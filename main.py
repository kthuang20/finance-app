# import necessary packages
import pandas as pd
import streamlit as st


st.title("Finance App")
'''This finance app takes in your yearly transactions to help you understand how much you saved and spent.'''

# ask the user to upload their transactions
st.sidebar.header("Upload your transactions:")
file = st.sidebar.file_uploader(label="Upload your transactions", type=["csv", "xlsx"])

# if the user has uploaded their file:
if file is not None:
	## read in as a dataframe
	transactions = pd.read_csv(file)
	st.write(transactions.head())