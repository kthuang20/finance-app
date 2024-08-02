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
	Managing multiple accounts ranging from checking and savings to retirement accounts can be challenging, 
	especially when they are scattered across different platforms. Analyzing personal finances manually each 
	month is time-consuming and cumbersome. While existing finance apps offer some solutions, they often 
	require creating new accounts and can be costly. This inspired the creation of a finance app that 
	consolidates all your financial data without additional costs or complications.

	### How it Works
	To make managing finances easier, I have integrated a simple way to download transactions and investments 
	across all accounts, primarily using Fidelity. By following a few steps, you can gather all your financial 
	data without extra charges:
	Downloading Spending Transactions::
	1. Logged into [Fidelity](https://digital.fidelity.com/ftgw/digital/plan-summary/summary)
	2. Click *View details* in the Net Worth section
	3. Select the *Spending* tab
	4. Scroll down to the *All Transactions* section and click the *Download transactions* hyperlink
	5. Manually remove the title of "Spending Transactions" and labels underneath the table in Excel

	Downloading Investment Transactions::
	1. Log into your Fidelity account
	2. Select *Accounts & Trade* → *Full View*
	3. Select the *Investments* tab → *Transactions*
	4. Choose your date range
	5. Click the *Export Results* button

	### How To Use 
	This app allows you to analyze yearly spending transactions and investments separately without requiring 
	you to sign into your bank account. For those who are interested in obtaining financial freedom, it
	also tracks your progress towards reaching your crossover point (*the point at which your passive investment
	income surpasses your living expenses*). All analyses work up to a year's worth of data. To perform these 
	analyses, simply navigate to the desired analysis on the sidebar and upload your spending and/or 
	investment transactions. To see what analyses are performed, click on the example button.

	### Limitations
	The app was developed using data collected from Fidelity. While users can upload their own files, the 
	data must be structured similarly to the example files. Fidelity users can follow the provided steps, 
	while non-Fidelity users may need to manually adjust their data to match the required format.

	---
	*Source code and sample files used in this app are available at:* https://github.com/kthuang20/finance-app
'''
