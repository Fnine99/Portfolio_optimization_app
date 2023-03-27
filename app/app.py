import enum
import random
import time
from typing import List, Tuple

import requests
import streamlit as st

from streamlit_searchbox import st_searchbox

from ..data.data import fetch, fetch_search_list

@st.cache_data
def search_tickers():
    """
    function with list of tuples (label:str, value:any)
    """
    # you can use a nice default here
    if not searchterm:
        return []
    
def search_rnd_delay(searchterm: str) -> List[str]:
    print(f"searching... {searchterm}")
    time.sleep(random.randint(1, 5))
    return [f"{searchterm}_{i}" for i in range(10)]

#### application starts here ####

c1, c2, c3 = st.columns(3)


with st.sidebar:
    selected_value = st_searchbox(
        search_function=search_tickers,
        placeholder="Search Wikipedia",
        label="Search symbol",
        default="SOME DEFAULT",
        clear_on_submit=False,
        clearable=True,
        key="search_wikipedia_ids",
    )
    st.info(f"{selected_value}")

st.header("Other components for reference:")
st.multiselect(
    "Multiselect",
    [1, 2, 3, 4, 5],
    default=[1, 2],
    key="multiselect",
)


c1, c2, c3 = st.columns(3)

with c1:
    selected_value2 = st_searchbox(
        search_sth_fast,
        default=None,
        label="search_sth_fast",
        clear_on_submit=True,
        key="search_sth_fast",
    )
    st.info(f"{selected_value2}")

with c2:
    selected_value3 = st_searchbox(
        search_rnd_delay,
        default=None,
        clear_on_submit=False,
        clearable=True,
        label="search_rnd_delay",
        key="search_rnd_delay",
    )
    st.info(f"{selected_value3}")

with c3:
    st.multiselect("For visual reference", [1, 2, 3], default=[1, 2])

st.markdown("---")

st.write("search_fancy_return (no label)")

selected_value4 = st_searchbox(
    search_fancy_return,
    clear_on_submit=True,
    key="search_fancy_return",
)
st.info(f"{selected_value4} {type(selected_value4)}")


st.markdown("---")
st.header("Other components for reference:")
st.multiselect(
    "Multiselect",
    [1, 2, 3, 4, 5],
    default=[1, 2],
    key="multiselect",
)
st.selectbox(
    "Selectbox",
    [1, 2, 3],
    index=1,
    key="selectbox",
)


