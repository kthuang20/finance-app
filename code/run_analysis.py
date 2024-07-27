import pandas as pd
import streamlit as st

### function to set up the data
def setup_data(file):
	## read the file as a dataframe
	transactions = pd.read_csv(file)
	
	return transactions