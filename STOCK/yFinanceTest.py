import yfinance as yf
import pandas
import numpy
import nasdaqModule
import json
import timeit
import datetime
#import lxml

x = datetime.datetime.now()
today = x.strftime("%x")
print(today)
"""----------------------------------------------------------------------------------------------------------------------------------------"""
start = datetime.datetime.now()
history = []
columnHeaders = ()
tickers = nasdaqModule.nasdaqTickers
"""for x in tickers:
    DIS = yf.Ticker(x)

    DISHist = DIS.history(period = "max")
    history.append(DISHist)"""
test = yf.Ticker("DIS")


history = test.history(period="max")
#print(typeGotten)

print(history)
finish = datetime.datetime.now()
"""for column in history.Columns:
    columnHeaders.append(column)"""
#historyJson = json.dumps(history)
"""print( help(nasdaqModule))
print(dir(nasdaqModule))
for x in nasdaqModule.nasdaqTickers:
    print(x)"""
#RETURNS---
#- ACAMW: 1d data not available for startTime=-2208988800 and endTime=1583274119. Only 100 years worth of day granularity data are allowed to be fetched per request.
#---FOR EACH STOCK
#Turns out that the yfinance is good for one request at a time.
#print(finish - start)
#savePath = "STOCK/LOG/history.csv"
"""doc = open(savePath,"a")
doc.write(historyJson)
doc.close()"""
historyDict = history.to_dict()
#history.to_csv(r'STOCK/LOG/history.csv')
#print(history.Columns)
print(start)

print(finish)

print(finish - start)
# this is how to grab an individual value -- print(historyDict.get("Open"[1]))
for x in historyDict:
    print(x)