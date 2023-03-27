import requests
import json
import datetime

url="https://api.twelvedata.com/time_series"

def get_api_key() -> str:
    file = open("api.txt", "r")
    api_key:str = file.readline().rstrip() 
    file.close()
    return api_key

def fetch(ticker:str) -> json:
    api_key=get_api_key()
    if (len(api_key)<1): 
        print("make sure you created the file <api.txt> and its content is in the right format.")
        return
    try: 
        res = requests.get(url,
            params={
                "symbol":ticker,
                "interval":"1month",
                "outputsize":"60",
                "api_key":api_key
            },
            timeout=5
        )
        if res.status_code==200: return res.json()
        else: print(f"Error fetching data: {res.status_code}")
    except requests.exceptions.RequestException as error:
        print("Error:", error)

url="https://api.twelvedata.com/stocks"

def fetch_search_list(ticker:str):
    res = requests.get(url,
            params={"symbol":ticker},
            timeout=5                   
        )
    if res.status_code == 200: return res.json()
    else: print(f"Error fetching data: {res.status_code}")
    

