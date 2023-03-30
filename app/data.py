import requests
import json
import datetime
    
def get_api_key() -> str:
    file = open("app/api.txt", "r")
    api_key:str = file.readline().rstrip() 
    file.close()
    return api_key

api_key=get_api_key()

def fetch(ticker_list:list) -> json:
    url="https://api.twelvedata.com/time_series"
    ticker = ''
    for tick in ticker_list:
        if ticker_list[-1]!= tick: ticker+=f"{tick},"
        else: ticker+=f"{tick}"

    print(ticker)
    if (len(api_key)<1): 
        print("make sure you created the file <api.txt> and its content is in the right format.")
        return
    try: 
        res = requests.get(url,
            params={
                "symbol":ticker,
                "interval":"1month",
                "outputsize":"60",
                "apikey":api_key
            },
            timeout=5
        )
        if res.status_code==200: return res.json()
        else: print(f"Error fetching data: {res.status_code}")
    except requests.exceptions.RequestException as error:
        print("Error:", error)



def fetch_search_list():
    url="https://api.twelvedata.com/stocks?"
    res = requests.get(url,
            params={"apikey":api_key},
            timeout=5                   
        )
    if res.status_code == 200: return res.json()
    else: print(f"Error fetching data: {res.status_code}")

if __name__ == "__main__":
    print(fetch(["aapl","pltr"]))