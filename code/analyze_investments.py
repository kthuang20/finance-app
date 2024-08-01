import pandas as pd
import streamlit as st
import plotly.express as px

### function to set up the data
def setup_data(file):
	## read the file as a dataframe
	transactions = pd.read_csv(file)

	## remove rows representing cash holdings
	cash_tickers = ["QPCTQ", "SPAXX"]
	transactions = transactions[~transactions["Ticker"].isin(cash_tickers)]
	transactions = transactions[transactions["Ticker"].notna()]

	## create three new columns for the date column: year, month, day
	transactions["Date"] = pd.to_datetime(transactions["Date"])
	transactions['Year'] = transactions['Date'].dt.year
	transactions['Month'] = transactions['Date'].dt.month
	transactions['Day'] = transactions['Date'].dt.day

	## convert the amount into numerical values
	transactions["Amount"] = transactions["Amount"].str.replace('$', '')
	transactions["Amount"] = transactions["Amount"].str.replace('(', '-')
	transactions["Amount"] = transactions["Amount"].str.replace(')', '')
	transactions["Amount"] = transactions["Amount"].astype(float)

	## make sure that buying are represented with positive amounts 
	transactions.loc[transactions["Type"] == "Buy", "Amount"] = transactions["Amount"].abs()
	transactions.loc[transactions["Type"] == "Sell", "Amount"] = -transactions["Amount"].abs()

	## separate the transactions into 2 separate dataframes: investments and dividends
	dividends = transactions[transactions["Type"] == "Income Dividend"]
	investments = transactions.drop(dividends.index)

	return investments, dividends


### function to visualize amount of investments added each month
def show_monthly_investments(investments):
	## create a dataframe with the total amount invested in ticker for each month
	monthly_investments = investments.groupby(["Month", "Ticker"])["Amount"].sum().reset_index()

	## add a column with the month names
	month_names = {1: "January",
				   2: "February",
				   3: "March",
				   4: "April",
				   5: "May",
				   6: "June",
				   7: "July",
				   8: "August",
				   9: "September",
				   10: "October",
				   11: "November",
				   12: "December"}
	## create a list of all the labels for the tabs, one for each ticker and last one for total
	all_tickers = monthly_investments["Ticker"].unique().tolist()
	tab_labels = ["All Investments"] + all_tickers

	## create tabs for all tickers + one combining all investments
	tabs = st.tabs(tab_labels)

	## for the last tab,
	with tabs[0]:
		# create a dataframe summarizing all the investments made per month
		all_data = monthly_investments.groupby("Month")["Amount"].sum().reset_index()

		# create a bar plot showing the total investments across all tickers
		fig = px.bar(all_data, x="Month", y="Amount", 
				 	 title = f"Total Investments Made Per Month")

		# update y-axis label
		fig.update_layout(yaxis_title="Amount (in $)")

		# replace the months with the month names
		fig.update_xaxes(
            tickvals=list(month_names.keys()),  # Numeric month values
            ticktext=[month_names[i] for i in month_names.keys()]  # Month names
        )

	    # show bar plot
		st.plotly_chart(fig)

	## for each of the other remaining ticker tabs,
	for ticker, tab in zip(all_tickers, tabs[1:]): 
		# select the data for that ticker
		ticker_data = monthly_investments[monthly_investments["Ticker"] == ticker]
		
		with tab:
			# create a bar plot showing the amount investment per month for that ticker
			fig = px.bar(ticker_data, x="Month", y="Amount", 
				 		 title = f"Monthly Investments Made For {ticker}")

			# update y-axis label
			fig.update_layout(yaxis_title="Amount (in $)")

			# replace the months with the month names
			fig.update_xaxes(
            	tickvals=list(month_names.keys()),  # Numeric month values
            	ticktext=[month_names[i] for i in month_names.keys()]  # Month names
        	)

	        # show bar plot
			st.plotly_chart(fig)


### function to show a pie chart describing the types of investments made
def show_investment_types(investments, col):
	## get the total investments made across all months for each ticker
	ticker_totals = investments.groupby("Ticker")["Amount"].sum().reset_index()

	## create and show a pie chart showing the 
	fig = px.pie(ticker_totals, values="Amount", names="Ticker", title="Types of Investments Made")
	col.plotly_chart(fig)

### function to show a pie chart describing the types of investments made
def show_dividends(dividends, col):
	## get the total investments made across all months for each ticker
	ticker_totals = dividends.groupby("Ticker")["Amount"].sum().reset_index()

	## create and show a pie chart showing the 
	fig = px.pie(ticker_totals, values="Amount", names="Ticker", title="Types of Dividends Earned")
	col.plotly_chart(fig)


### function to generate the summary statistics
def sum_stats(investments, dividends):
	## calculate the total amount invested and total dividends earned
	total_invested = investments["Amount"].sum()
	total_dividends = dividends["Amount"].sum()

	## find the ticker the user invested in the most
	ticker_investments = investments.groupby("Ticker")["Amount"].sum().reset_index()
	highest_ticker_invested = ticker_investments.sort_values("Amount", ascending=False).iloc[0, 0]
	## calculate percent of all investments this ticker was made up of
	highest_investment = ticker_investments.sort_values("Amount", ascending=False).iloc[0, 1]
	percent_invested = highest_investment/float(total_invested) * 100

	## find the ticker that earned the most amount of dividends
	ticker_dividends = dividends.groupby("Ticker")["Amount"].sum().reset_index()
	highest_ticker_dividend = ticker_dividends.sort_values("Amount", ascending=False).iloc[0, 0]
	## calculate percent of all dividends this ticker's was made up of
	highest_dividend = ticker_dividends.sort_values("Amount", ascending=False).iloc[0, 1]
	percent_dividend = highest_dividend/float(total_dividends) * 100


	## show user the results
	st.header("Summary Statistics")
	st.write("You:")
	st.write(f"* Invested a total of ${total_invested:,.2f}, \
		with {highest_ticker_invested} making up {percent_invested:.2f}% of your total investments")
	st.write(f"* Earned a total of ${total_dividends:,.2f} in dividends, \
		with {highest_ticker_dividend} making up {percent_dividend:.2f}% of your total dividends")