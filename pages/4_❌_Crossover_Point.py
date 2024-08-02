### import necessary packages
import pandas as pd
import streamlit as st

### configure settings of page
st.set_page_config(
	layout = "wide",
	initial_sidebar_state = "expanded")

### in the sidebar,
with st.sidebar:
	### add a note to make sure user format the files correctly
	st.write("*Note:* This analysis only works using .csv files formatted like the example \
		[spending transactions](https://github.com/kthuang20/finance-app/raw/main/sample_data/spending_transactions.csv) \
		and [investments](https://github.com/kthuang20/finance-app/raw/main/sample_data/InvestmentTransactions.csv) files")
	### add a file uploader section to upload spending transactions
	spending_file = st.file_uploader("Upload your spending transactions here:", type=".csv")
	### add a file uploader section to upload investment transactions
	investments_file = st.file_uploader("Upload your investment transactions here:", type=".csv")

	### add a button to allow user to try example files
	st.write("Or try using example files")
	try_example = st.button("Example files")

