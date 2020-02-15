from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import requests
import webbrowser
import csv
import json
import datetime #import date
import os

url = URLArrayElement 
      page = requests.get(url)    
      soup = BeautifulSoup(page.content, 'html.parser')
      quotes = soup.find("table", class_ ="quotes")
      return quotes