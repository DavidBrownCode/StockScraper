rows = ["bbb","better business bureau", 123.01, 122.99]
NASDAQJson = {}
class NASDAQ:
    def __init__(self, symbol, company, high, low):
        self.symbol = rows[0]
        self.company = rows[1]
        self.high = rows[2]
        self.low = rows[3]

    def NASDAQJson(self, symbol,company,high, low):
        symbol = {
            "symbol": symbol,
            "company": company,
            "high": high,
            "low": low  
        }
    
NASDAQJson.append(symbol)

for x in NASDAQJson:
    print(x)