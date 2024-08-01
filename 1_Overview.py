### import necessary packages
import streamlit as st
import pandas as pd

### configure settings of page
st.set_page_config(
	page_title = "Finance App",
	page_icon = "💰",
	layout = "wide",
	initial_sidebar_state = "expanded")

### add name to sidebar
st.sidebar.markdown("*Created by [Katie Huang](https://kthuang20.github.io/Katie_Portfolio/)*")

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
	download transactions and investments across all accounts that doesn't cost money. To do this, I 
	first linked all my accounts (internal and external) in Fidelity.

	To download all my spending transactions, I:
	1. Logged into this website: https://digital.fidelity.com/ftgw/digital/plan-summary/summary
	2. In the Net Worth section, clicked *View details*
	3. Selected the *Spending* tab
	4. Scrolled down to the *All Transactions* section and clicked the *Download transactions* hyperlink
	5. I manually removed the title of "Spending Transactions" and labels underneath the table in Excel

	To download all my investment transactions, I:
	1. Logged into my Fidelity account
	2. Selected *Accounts & Trade* → *Full View*
	3. Selected the *Investments* tab → *Transactions*
	4. Selected date range of interest
	5. Clicked the *Export Results* button
	

	### How To Use 
	I have designed this finance app to your analyze yearly spending transactions and investments separately. 
	In attempts to make it safer, this app does not require you to sign into your bank account. Instead, it
	allows you upload files with your spending and investments transactions up to a years worth of transactions.
	Once you have uploaded your own file, it will automatically generate a dashboard analyzing your transactions.
	Click on the sidebar on the left to navigate to which analysis you would like to perform. 

	### Limitations
	I created this app using data that I collected from Fidelity. This means that while the app allows the user 
	to upload their file, the files would need to be structured like the example files. For Fidelity users,
	they would need to perform the steps that I have described up above. For non-Fidelity users, they would
	need to manually structure their data as the example files.

	---
	*Source code and sample files used in this app is available at:* https://github.com/kthuang20/finance-app
'''
