import requests
import random
import time
import streamlit as st
from typing import List, Dict
from streamlit_searchbox import st_searchbox


def fetch_search_list(api_key: str, symbol: str = "") -> Dict:
    url = "https://api.twelvedata.com/stocks"
    params = {"symbol": symbol, "apikey": api_key, "exchange": "NASDAQ", "country": "United States"}
    try:
        res = requests.get(url, params=params, timeout=5)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.write(f"Error fetching data: {e}")
        return {}
    return res.json()


def process_options(api_key: str, symbol: str) -> List[str]:
    if not symbol:
        return []
    st.write(f"Searching for {symbol}...")
    time.sleep(random.randint(0, 1))
    data = fetch_search_list(api_key, symbol)
    return [tick["symbol"] for tick in data.get("data", [])]


def get_options_data(api_key: str, selected_options: Dict) -> Dict:
    symbols = list(selected_options.values())
    symbols_str = ",".join(symbols)
    url = "https://api.twelvedata.com/time_series"
    params = {"symbol": symbols_str, "apikey": api_key, "interval": "1day", "outputsize": "30"}
    try:
        res = requests.get(url, params=params, timeout=5)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.write(f"Error fetching data: {e}")
        return {}
    return res.json()


# States

if "selected_options" not in st.session_state:
    st.session_state.options_count = 0
    st.session_state.selected_options = {}

# Set up page config and title

st.set_page_config(page_title="My Landing Page", page_icon=":rocket:", initial_sidebar_state="collapsed")
st.title("Welcome to My Landing Page!")

# Add search box widget to sidebar

input_value = st.sidebar.text_input(
    "Search for a stock ticker:",
    key=f"search_symbol_{st.session_state.options_count}",
    help="Type the name or symbol of a stock to search for.",
)

if input_value:
    options = process_options("api_key", input_value)
    selected = st.sidebar.multiselect(
        "Select one or more tickers to search for:",
        options,
        default=[],
    )
    for symbol in selected:
        if symbol not in st.session_state.selected_options.values():
            st.session_state.selected_options[st.session_state.options_count] = symbol
            st.session_state.options_count += 1
