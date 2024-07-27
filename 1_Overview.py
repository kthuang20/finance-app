### import necessary packages
import streamlit as st
import pandas as pd

### create a multiple pages
st.set_page_config(
	page_title="Finance App",
	page_icon="💰"
	)

'''
	# Finance App 💰
	*Welcome to a personal finance app that provides insights into your spending and saving habits and 
	investments. This app aims to help you understand your progress and guide you towards your financial goals.*
	
	### Inspiration
	I have multiple accounts ranging from my checkings and savings to retirement accounts.
	However, because they were located in various locations, keeping track of everything 
	going in and out has been challenging. It is cumbersome to have to painstakingly analyze my own 
	finances every month for an entire year. While I have looked into finance apps, many of those 
	available currently require you to create another account to link all your bank accounts. Many also
	cost money to access their resources and tools to analyze your finances. 
	Hence, this finance app was born.
	
	I have many of my accounts at Fidelity and through some fiddling around, I found a simple way to 
	download transactions and investments across all accounts that doesn't cost money.
	Here are the following steps I performed on my laptop:
	1. Link all your accounts (internal and external) in Fidelity.
	2. Under the Accounts & Trade tab, select *Full View*
	3. To download all spending transactions, select *Spending → Transactions → Export Results*
	4. To download all investment transactions, select *Investments → Transactions → Export Results*


	### How To Use 
	I have designed this finance app to your analyze yearly spending transactions and investments separately.
	Click on the sidebar to navigate to which analysis you would like to perform.

	---
	*Source code for this app is available at:* https://github.com/kthuang20/finance-app


'''