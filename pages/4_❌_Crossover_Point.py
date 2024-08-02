### import necessary packages
import pandas as pd
import streamlit as st

### import self written functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_both import setup_data, show_crossover, gen_sum

### configure settings of page
st.set_page_config(
	layout = "wide",
	initial_sidebar_state = "expanded")

### in the sidebar,
with st.sidebar:
	## add a note to make sure user format the files correctly
	st.write("*Note:* This analysis only works using .csv files formatted like the example \
		[spending transactions](https://github.com/kthuang20/finance-app/raw/main/sample_data/spending_transactions.csv) \
		and [investments](https://github.com/kthuang20/finance-app/raw/main/sample_data/InvestmentTransactions.csv) files")
	## add a file uploader section to upload spending transactions
	spending_file = st.file_uploader("Upload your spending transactions here:", type=".csv")
	## add a file uploader section to upload investment transactions
	investments_file = st.file_uploader("Upload your investment transactions here:", type=".csv")

	## add a button to allow user to try example files
	try_demo = st.button("Example files")

	### add credits to sidebar
	st.markdown('''
		--- 
		*Created by [Katie Huang](https://kthuang20.github.io/Katie_Portfolio/)*''')

### function to create the dashbaord
def create_dashboard(spending_file, investments_file):
	## setup the data needed to further analysis
	monthly_expenses, monthly_investments = setup_data(spending_file, investments_file)
	## create a line plot comparing monthly expenses to investment income
	show_crossover(monthly_expenses, monthly_investments)
	## show description of results
	gen_sum(monthly_expenses, monthly_investments)

### add title to main page
st.title("Crossover Point Update")

### if the user uploaded their own files,
if spending_file is not None and investments_file is not None:
	## create the dashboard
	create_dashboard(spending_file, investments_file)

### otherwise, if the demo button is clicked
elif try_demo:
	## create the dashboard
	spending_url = "https://github.com/kthuang20/finance-app/raw/main/sample_data/spending_transactions.csv"
	investments_url = "https://github.com/kthuang20/finance-app/raw/main/sample_data/InvestmentTransactions.csv"
	create_dashboard(spending_url, investments_url)

