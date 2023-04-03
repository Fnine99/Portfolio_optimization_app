import streamlit as st
from streamlit_searchbox import st_searchbox

import random
import time

from data import fetch_search_list, fetch

def get_options(symbol:str):
    if not symbol: return []
    print(f"searching... {symbol}")
    time.sleep(random.randint(0,1))
    data = fetch_search_list(symbol)
    return [tick['symbol'] for tick in data['data']]

def get_options_data(selected_options):
    data = fetch(selected_options)
    return data

## states

if "selected_options" not in st.session_state:
    st.session_state.options_count=0
    st.session_state.selected_options = {}

st.set_page_config(page_title="My Landing Page", page_icon=":rocket:", initial_sidebar_state="collapsed")

st.title("Welcome to My Landing Page!")

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel ante hendrerit, lobortis est eget, ultricies velit. Nam at dui vitae ipsum laoreet finibus.")

input_value = st_searchbox(
    get_options,
    clear_on_submit=True,
    key=f"search_symbol_{st.session_state.options_count}",
    placeholder="Search any ticker",
)

if input_value and str(input_value) not in st.session_state.selected_options.items(): 
    st.session_state.selected_options[st.session_state.options_count] = input_value
    st.session_state.options_count+=1

if st.button("search"):
    data = get_options_data()

st.write("selected", st.session_state.get("selected_options"))
st.markdown("---")

print(list(st.session_state.get("selected_options").values()))
