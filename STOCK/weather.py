from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import requests
import webbrowser
import csv
import json
import datetime #import date
import os

rowArray = []
def getTable():
    url = "https://weather.com/weather/tenday/l/52a4300963a4d71cf5be76f6d043e66982a6dc6ab73e40b91d9db21e1c600d04" 
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    """forecast = soup.find("table", class_ ="twc-table")
    rows = forecast.findAll("tr")
    for row in rows:
        print(row)pip
        rowArray.append(row)
    #print(foreca
    return rowArray"""

#print(getTable())

