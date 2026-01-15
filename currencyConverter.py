import requests
API_KEY = "fca_live_JLvTUs028gfklVnrWE7hBaBljLakCOndcO55wFfa"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "CAD", "AUD", "CNY"]

def currency_converter(base):
    currencies = ",".join(CURRENCIES)
    URL = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:

        response = requests.get(URL)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None
        
    
while True:
    base = input("Enter the base currency (q to quit)").upper()

    if (base == "Q"):
        break

        
    data = currency_converter(base)

    if not data:
        continue

    del data[base]

    for key,value in data.items():
        print (f"{key}: {value}")
        



    

    


    

        

