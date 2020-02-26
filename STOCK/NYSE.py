from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import requests
import webbrowser
import csv
import json
import datetime #import date
import os

x = datetime.datetime.now()
today = x.strftime("%x")
print(today)
year =  x.strftime("%Y")
dayofmonth =  x.strftime("%d")
month =  x.strftime("%B")
"""The website seperates the stocks by alphabetical order and ea/ch letter has a page.  I could have gone through
the href of the section that holds the the alphabet at the top but I thought this would be easier.
The other problem is that, given the look of the website, I don't trust that the site is properly updated.
The Stock symbols will have to be verified.---I changed the website to another website similarly constructed.  The current website returns 
stock information which can be used for quick verification.  I also now have the ability to change betweem markets.  So now I can gather information from the New York Stock Exchange or even foreign markets."""

URLPart1 = "http://www.eoddata.com/stocklist/NYSE/"
#MarketArray = ["NYSE","NYSE","INDEX"]
#URLPart2 = "/"
URLPart2 = ".htm"
alphabeticalArray = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
URLArray = []
tArray =[]
rowArray = []

NYSEJson = []
def getTable(alphabeticalArray):
   #for market in MarketArray:
   for alpha in alphabeticalArray:
      URLArrayElement = URLPart1 + alpha + URLPart2
      url = URLArrayElement 
      page = requests.get(url)    
      soup = BeautifulSoup(page.content, 'html.parser')
      quotes = soup.find("table", class_ ="quotes")
      #return = market
      return quotes


for x in alphabeticalArray:
   t = getTable(x)
   if(t != None):
      txt = t.text
      tArray.append(txt)
      rows = t.findAll("tr", class_ = "re" or "ro")
      y = 1
      for row in rows:
         cellArray = []
         cells = row.findAll("td")
         for cell in cells:
            cellTXT = cell.text
            cellArray.append(cellTXT)         
         rowArray.append(cellArray)               
   else:
      continue

#print(rowArray[][0])

for row in rowArray:
   dictName = row[0]
   symbol = dictName
   company = row[1]
   high = row[2]
   low = row[3]
   close = row[4]
   change = row[6]
   #open = (int(close) - int(change))
   dictName = {
      "date": today,
      "market": "NYSE",
      "symbol": symbol,
      "company": company,
      "high": high,
      "low": low,
      "close": close,
      #"open": int(close)-int(change),
      "change": change
      #"change":high - low
   }
   NYSEJson.append(dictName)
print(len(NYSEJson))
"""print(NYSEJson[763:767])
for dic in NYSEJson:
   doc = open("../../Python/Stock.txt", "a")
   doc.write(str(dic))
   doc.close()"""

y = json.dumps(NYSEJson)
NYSEJson = y
#print(NYSEJson)
savePath = "STOCK/LOG/" + dayofmonth + month + year + "NYSE.json"
if os.path.exists(savePath):
   pass
else:
   doc = open(savePath,"a")
   doc.write(NYSEJson)
   doc.close()

symbolList = []
for x in rowArray:
   #print(x[0])
   symbolList.append(x[0])

symbolTuple = tuple(symbolList)
sym = open("STOCK/NYSEModule.py", "w")
sym.write("NYSETickers = [")
for x in symbolList[0:(len(symbolList)-1)]:
   sym.write('"' + x + '"' + ",")
sym.write('"' + symbolList[-1] + '"')
sym.write("]")
sym.close()

yahooFinanceArray = []