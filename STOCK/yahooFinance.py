from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import requests
import webbrowser
import csv
import json
import datetime #import date
import os
from nasdaqModule import nasdaqTickers
singleTest = "VZ"
listTest = ["VZ","TSLA","WDC","ZBRA"]
url1 = "https://finance.yahoo.com/quote/"
url2 = "history?p="
url = url1 + singleTest + url2 + singleTest
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
app = soup.find("div", id = "app")
step1 = app.find("div", reactid ="1")
step2 = step1.find("div", reactid ="2")
#table = app.find("tbody")
#cells = table.findAll("td")
"""for row in rows:
    print(row.text)"""
print(step2)

#print(soup)