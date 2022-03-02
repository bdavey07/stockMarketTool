import Common.lookups as lookup
from Common.lookups import Ticker

def main():
    while True:
        print("Enter the ticker symbol for the stock that you want to lookup or 'exit' to quit")
        tickerSymInput = input()
        if tickerSymInput.lower() == "exit":
            return
        else:
            stock = Ticker(tickerSymInput)
            print("\n" ,stock.price , "\n")
            print(stock.monthly)

if __name__ == "__main__":
    main()