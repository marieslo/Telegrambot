import requests

base_key = "RUB"
sym_key1 = "USD"
sym_key2 = "EUR"
amount = 1

r = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"
resp = json.loads(r.content)
print(resp)

