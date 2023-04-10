import streamlit as st
# from streamlit_searchbox import st_searchbox
from streamlit_tags import st_tags_sidebar, st_tags

from frontier import Frontier
from portfolio import Portfolio

import plotly.express as px
# import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np
import random
import time

from data import fetch_search_list, fetch

st.set_page_config(page_title="Porfolio Manager", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

def get_options(symbol:str):
    if not symbol: return []
    print(f"searching... {symbol}")
    time.sleep(random.randint(0,1))
    data = fetch_search_list(symbol)
    return [tick['symbol'] for tick in data['data']]

@st.cache_data
def get_data(tickers):
    return fetch(tickers)

if "tickers_data" not in st.session_state:
    st.session_state["tickers_data"] = get_data(["AAPL", "PLTR", "GOOG", "AMD", "NVDA", "BABA"])

@st.cache_data
def get_options_data(iterations=None, risk_free=None):
    portfolio = Portfolio(st.session_state.tickers_data)
    portfolio.compute()
    if iterations and risk_free: frontier = Frontier(portfolio, iterations=iterations, rf_rate=risk_free)
    else: frontier = Frontier(portfolio)
    frontier.compute()
    return portfolio, frontier

if "data" not in st.session_state:
    st.session_state["data"] = get_options_data()

# if "data" not in st.session_state:
#     get_data(["AAPL", "PLTR", "GOOG", "AMD", "NVDA", "BABA"])
#     st.session_state["data"] = get_options_data()

st.sidebar.title("Portfolio Manager")

st.sidebar.write("This project is an implementation of the Markowitz efficient frontier model of the modern portfolio theory. This Beta release will receive future updates.")

# st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", max_selections=None)
tickers = st_tags_sidebar(
    label='# Enter your symbols:',
    text='Press enter to add more',
    value=["AAPL", "PLTR", "GOOG", "AMD", "NVDA", "BABA"],
    # suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags = 6,
    key='1')

if st.sidebar.button("optimize"):
    st.session_state.tickers_data = get_data(tickers)
    st.session_state.data = get_options_data()

st.write(f"Current portfolio assets: {[ticker.upper() for ticker in tickers]}")
st.write(f"Weights: {st.session_state.data[0].portfolio_weights}")

overview_tab, statistics_tab, summary_tab = st.tabs(["Overview", "Statistics", "Summary"])



with overview_tab:
    with st.expander("Asset allocation", expanded=True):
        tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Min volatility lo", "Max Sharpe lo", "Min volatility op", "Max Sharpe op", "Max return op", "Max return lo"])

        with tab4:
            tab4_col1, tab4_col2 = st.columns((1,2))
            with tab4_col1:
                st.write('Located minimum volatility')
                st.dataframe(st.session_state.data[1].min_vol_port[:2], use_container_width=True)
            with tab4_col2:
                labels = list(st.session_state.data[1].min_vol_port.keys())[2:] 
                sizes = list(st.session_state.data[1].min_vol_port.values)[2:]
                fig = px.pie(values=sizes, names=labels)
                st.plotly_chart(fig, use_container_width=True)

        with tab5:
            tab5_1, tab5_2 = st.columns((1,2))
            with tab5_1:
                st.write('Located maximum Sharpe ratio')
                st.dataframe(st.session_state.data[1].optimal_risky_port[:2], use_container_width=True)
            with tab5_2:
                labels = list(st.session_state.data[1].optimal_risky_port.keys())[2:] 
                sizes = list(st.session_state.data[1].optimal_risky_port.values)[2:]
                fig = px.pie(values=sizes, names=labels)
                st.plotly_chart(fig, use_container_width=True)

        optimized_max_return_port = {
            "Returns":st.session_state.data[1].optimized_max_return_port[0],
            "Volatility": st.session_state.data[1].optimized_max_return_port[0],
        }
        for i in range(len(st.session_state.data[1].optimized_min_vol_port[2])):
            optimized_max_return_port[f"{st.session_state.data[0].tickers[i]} weight"] = st.session_state.data[1].optimized_min_vol_port[2][i]

        optimized_min_vol_port = {
            "Returns":st.session_state.data[1].optimized_min_vol_port[0],
            "Volatility": st.session_state.data[1].optimized_min_vol_port[0],
        }
        for i in range(len(st.session_state.data[1].optimized_min_vol_port[2])):
            optimized_min_vol_port[f"{st.session_state.data[0].tickers[i]} weight"] = st.session_state.data[1].optimized_min_vol_port[2][i]

        optimized_optimal_risky_port = {
            "Returns":st.session_state.data[1].optimized_optimal_risky_port[0],
            "Volatility": st.session_state.data[1].optimized_optimal_risky_port[0],
        }
        for i in range(len(st.session_state.data[1].optimized_min_vol_port[2])):
            optimized_optimal_risky_port[f"{st.session_state.data[0].tickers[i]} weight"] = st.session_state.data[1].optimized_optimal_risky_port[2][i]


        with tab6:
            tab6_1, tab6_2 = st.columns((1,2))
            with tab6_1:
                st.write('Optimized minimum volatility')
                st.dataframe(pd.DataFrame.from_dict(optimized_min_vol_port, orient='index', columns=['Min Vol'])[:2], use_container_width=True)
            with tab6_2:
                labels = list(optimized_min_vol_port.keys())[2:] 
                sizes = list(optimized_min_vol_port.values())[2:]
                fig = px.pie(values=sizes, names=labels)
                st.plotly_chart(fig, use_container_width=True)

        with tab7:
            tab7_1, tab7_2 = st.columns((1,2))
            with tab7_1:
                st.write('Optimized maximum Sharpe ratio')
                st.dataframe(pd.DataFrame.from_dict(optimized_optimal_risky_port, orient='index', columns=['Opt port'])[:2], use_container_width=True)
            with tab7_2:
                labels = list(optimized_optimal_risky_port.keys())[2:] 
                sizes = list(optimized_optimal_risky_port.values())[2:]
                fig = px.pie(values=sizes, names=labels)
                st.plotly_chart(fig, use_container_width=True)
        with tab8:
            tab8_1, tab8_2 = st.columns((1,2))
            with tab8_1:
                st.write('Optimized maximum return portfolio')
                st.dataframe(pd.DataFrame.from_dict(optimized_max_return_port, orient='index', columns=['Opt port'])[:2], use_container_width=True)
            with tab8_2:
                labels = list(optimized_max_return_port.keys())[2:] 
                sizes = list(optimized_max_return_port.values())[2:]
                fig = px.pie(values=sizes, names=labels)
                st.plotly_chart(fig, use_container_width=True)

        with tab9:
            tab4_col1, tab4_col2 = st.columns((1,2))
            with tab4_col1:
                st.write('Located maximum return portfolio')
                st.dataframe(st.session_state.data[1].max_return[:2], use_container_width=True)
            with tab4_col2:
                labels = list(st.session_state.data[1].max_return.keys())[2:] 
                sizes = list(st.session_state.data[1].max_return.values)[2:]
                fig = px.pie(values=sizes, names=labels)
                st.plotly_chart(fig, use_container_width=True)

    with st.expander("Portfolio optimization", expanded=True):
        slider, risk_free = st.columns((4,1))
        slider_value = 20000
        risk_free_rate = 4.5/100
        with slider:
            slider_value = st.slider("Select how many portfolios to model", 5000, 100000, value=slider_value)
        with risk_free:
            risk_free_rate = st.number_input("Risk free rate (%)", value=risk_free_rate/100, step=0.5)
        st.session_state.data = get_options_data(slider_value, risk_free_rate)

        portfolios = st.session_state.data[1].portfolios
            
        min_vol_port = portfolios.iloc[portfolios['Volatility'].idxmin()]
        max_return_port = portfolios.iloc[portfolios['Returns'].idxmax()]
        optimal_risky_port = portfolios.iloc[((portfolios['Returns']-st.session_state.data[1].rf_rate)/portfolios['Volatility']).idxmax()]

        fig = px.scatter(portfolios, x='Volatility', y='Returns', 
                        color='Volatility', color_continuous_scale='amp',
                        hover_data=list(portfolios.keys()[2:]),
                        title='Portfolio Optimization Results')
        fig.update_layout(
                        xaxis=dict(title='Volatility'),
                        yaxis=dict(title='Returns'),
                        xaxis_title="Volatility",
                        yaxis_title="Returns",
                        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="right", x=1),
                        width=800, height=600,
                        margin=dict(l=50, r=50, b=100, t=100, pad=4),
                        # plot_bgcolor='rgb(243, 243, 243)',
                        # paper_bgcolor='rgb(243, 243, 243)'
                        )
        fig.add_scatter(x=[st.session_state.data[1].optimized_min_vol_port[1]],
                        y=[st.session_state.data[1].optimized_min_vol_port[0]],
                        mode='markers', marker=dict(color='green', size=8, symbol='circle'),
                        name='Optimized minimum volatility portfolio')
        fig.add_scatter(x=[st.session_state.data[1].optimized_optimal_risky_port[1]],
                        y=[st.session_state.data[1].optimized_optimal_risky_port[0]],
                        mode='markers', marker=dict(color='cyan', size=8, symbol='circle'),
                        name='Optimized maximum Sharpe ratio portfolio')
        fig.add_scatter(x=[st.session_state.data[1].optimized_max_return_port[1]],
                        y=[st.session_state.data[1].optimized_max_return_port[0]],
                        mode='markers', marker=dict(color='blue', size=8, symbol='circle'),
                        name='Optimized maximum return portfolio')
        fig.add_scatter(x=[min_vol_port[1]], y=[min_vol_port[0]],
                        mode='markers', marker=dict(color='black', size=8, symbol='circle'),
                        name='Located minimum volatility portfolio')
        fig.add_scatter(x=[optimal_risky_port[1]], y=[optimal_risky_port[0]],
                        mode='markers', marker=dict(color='red', size=8, symbol='circle'),
                        name='Located maximum Sharpe ratio portfolio')
        fig.add_scatter(x=[max_return_port[1]], y=[max_return_port[0]],
                        mode='markers', marker=dict(color='purple', size=8, symbol='circle'),
                        name='Located maximum return portfolio')
        st.plotly_chart(fig, theme="streamlit", use_container_width=True, height=800)
    
    with st.expander("See explanation", expanded=True):
        col3, col4 = st.columns(2)
        with col3:
            test = pd.DataFrame(st.session_state.data[0].monthly_returns, st.session_state.data[0].dates[:st.session_state.data[0].min_length-1])
            fig = px.line(test, x=test.index, y=test.columns, title="Monthly Returns")
            fig.update_layout(showlegend=True, xaxis_title="Date", yaxis_title="Returns")
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)

        with col4:
            test3 = pd.DataFrame.from_dict(st.session_state.data[0].stdev, orient='index', columns=['Standard Deviation'])
            fig = px.bar(test3, x=test3.index, y='Standard Deviation')
            fig.update_layout(title="Volatility", xaxis_title="Stock", yaxis_title="Volatility")
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
with statistics_tab:
    with st.expander("Assets correlation", expanded=True):
        corr_matrix = st.session_state.data[0].correlation_matrix
        fig = px.imshow(corr_matrix, text_auto=True,
                        aspect="auto",
                        x=st.session_state.data[0].tickers,y=st.session_state.data[0].tickers,
                        color_continuous_scale='amp')
        fig.update_xaxes(side="top")
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    
    with st.expander("Assets covariance", expanded=True):
        cov_matrix = st.session_state.data[0].covariance_matrix
        fig = px.imshow(cov_matrix, text_auto=True,
                        aspect="auto",
                        x=st.session_state.data[0].tickers,y=st.session_state.data[0].tickers,
                        color_continuous_scale='amp')
        fig.update_xaxes(side="top")
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with summary_tab:
    with st.expander("Monthly prices", expanded=True):
        monthly_prices = pd.DataFrame(st.session_state.data[0].monthly_prices, st.session_state.data[0].dates[:st.session_state.data[0].min_length])
        st.dataframe(monthly_prices.style.highlight_max(color="green",axis=0).highlight_min(color="red",axis=0), use_container_width=True, height=500)
    with st.expander("Monthly returns", expanded=True):
        table, chart = st.columns((2, 3))
        with table: 
            monthly_returns = pd.DataFrame(st.session_state.data[0].monthly_returns, st.session_state.data[0].dates[:st.session_state.data[0].min_length-1])
            st.dataframe(monthly_returns.style.highlight_max(color="green",axis=0).highlight_min(color="red",axis=0), use_container_width=True, height=500)
        with chart:
            df = pd.DataFrame({'Stock': list(st.session_state.data[0].arith_mean_returns.keys())*2,
                'Returns': list(st.session_state.data[0].arith_mean_returns.values()) + list(st.session_state.data[0].geo_mean_returns.values()),
                'Type': ['Arithmetic']*len(st.session_state.data[0].arith_mean_returns) + ['Geometric']*len(st.session_state.data[0].geo_mean_returns)})

            fig = px.bar(df, x='Stock', y='Returns', color='Type',
                        barmode='group', height=400, template='plotly_dark')

            fig.update_layout(title='Mean Returns', xaxis_title='Stocks', yaxis_title='Returns')

            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
