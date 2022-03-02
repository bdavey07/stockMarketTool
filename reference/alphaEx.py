from Resources.apikey import ALPHA_KEY
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=ALPHA_KEY'
r = requests.get(url)
data = r.json()

f = open("tempFile.json", "w")
f.write(print(data))
f.close()