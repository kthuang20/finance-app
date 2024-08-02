### import necessary packages
import pandas as pd
import plotly.express as px
import plost

### import self written functions used to analyze the data
import sys
sys.path.append("code/")
from analyze_spending import setup_data as setup_spending
from analyze_investments import setup_data as setup_investments
