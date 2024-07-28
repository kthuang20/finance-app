import pandas as pd
import streamlit as st
import plotly.express as px

### function to set up the data
def setup_data(file):
	## read the file as a dataframe
	transactions = pd.read_csv(file)

	## create three new columns for the date column: year, month, day
	transactions["Date"] = pd.to_datetime(transactions["Date"])
	transactions['Year'] = transactions['Date'].dt.year
	transactions['Month'] = transactions['Date'].dt.month
	transactions['Day'] = transactions['Date'].dt.day

	## convert the amount into numerical values
	transactions["Amount"] = pd.to_numeric(transactions["Amount"])

	return transactions