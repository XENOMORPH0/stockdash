import streamlit as st, numpy as np, yfinance as yf
import plotly.express as px

st. title('Stock Dashboard')
ticker = st.sidebar.text_input ('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

import plotly.express as px
fig = px.line(yf, x='date', y='price')
st.plotly_chart(fig)

