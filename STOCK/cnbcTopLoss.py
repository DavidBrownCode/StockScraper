from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import requests
import webbrowser
import csv
import json
import datetime #import date
import os

url = "https://www.cnbc.com/us-market-movers/"
page = requests.get(url)    
soup = BeautifulSoup(page.content, 'html.parser')
mainContent = soup.find("div", id = "MainContent")
#
# 
step3 = mainContent.find("div", class_ = "PageBuilder-col-9 PageBuilder-col")
step4 = step3.find("section", class_ = "MarketMovers-marketTopContainer MarketMovers-marketTopContainerStacked")
step5 = step4.find("section", class_ = "marketTop = mainContent.find")
#marketTop = step3.findAll("section")
#, class_ = "MarketTop-fullWidthContainer")
step6 = step4.find_all("div", {'class' : "MarketMovers-loadingContainer"})
table = step4.find("table", {'class': "MarketTop-topTable"})
print(table)