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

URLPart1 = "http://www.eoddata.com/stocklist/NASDAQ/"
URLPart2 = ".htm"
alphabeticalArray = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
URLArray = []
tArray =[]
rowArray = []

nasdaqJson = []
def getTable(alphabeticalArray):
   for alpha in alphabeticalArray:
      URLArrayElement = URLPart1 + alpha + URLPart2
      url = URLArrayElement 
      page = requests.get(url)    
      soup = BeautifulSoup(page.content, 'html.parser')
      quotes = soup.find("table", class_ ="quotes")
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
   dictName = {
      "date": today,
      "market": "NASDAQ",
      "symbol": symbol,
      "company": company,
      "high": high,
      "low": low,
      "close": close
      #"change":high - low
   }
   nasdaqJson.append(dictName)
print(len(nasdaqJson))
"""print(nasdaqJson[763:767])
for dic in nasdaqJson:
   doc = open("../../Python/Stock.txt", "a")
   doc.write(str(dic))
   doc.close()"""

y = json.dumps(nasdaqJson)
nasdaqJson = y
#print(nasdaqJson)
if os.path.exists("STOCK/LOG/" + dayofmonth + month + year + "NASDAQ.json"):
   pass
else:
   doc = open("STOCK/LOG/" + dayofmonth + month + year + "NASDAQ.json","a")
   doc.write(nasdaqJson)
   doc.close()

symbolList = []
for x in rowArray:
   #print(x[0])
   symbolList.append(x[0])

symbolTuple = tuple(symbolList)
sym = open("STOCK/nasdaqModule.py", "w")
sym.write("nasdaqTickers = [")
for x in symbolList[0:(len(symbolList)-1)]:
   sym.write('"' + x + '"' + ",")
sym.write('"' + symbolList[-1] + '"')
sym.write("]")
sym.close()

yahooFinanceArray = []

"""def getClosing(d):
   for x in symbolList:
      yahooFinance = "https://finance.yahoo.com/quote/" + x + "?p=" + x
      #find("span", class_  = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
      page = requests.get(yahooFinance)    
      soup = BeautifulSoup(page.content, 'html.parser')
      closing = soup.findAll("span", class_  = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
      closing = closing
      return closing
z
print(getClosing(symbolList))"""

"""for x in symbolList:
   yahooFinance = "https://finance.yahoo.com/quote/" + x + "?p=" + x
   #find("span", class_  = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
   page = requests.get(yahooFinance)    
   soup = BeautifulSoup(page.content, 'html.parser')
   closing = soup.find("span", class_  = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
   closing = closing.text
   print(x, closing)"""