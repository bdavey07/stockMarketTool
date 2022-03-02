from yahoo_fin import stock_info as si

aaplPrice = si.get_live_price("amzn")

print(aaplPrice)