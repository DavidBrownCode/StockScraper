from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import requests
import webbrowser
import csv
import json
import datetime #import date
import os


url = "filename"
page = requests(url)

parsed = BeautifulSoup(page.content, "html.parser")

"""pretty = prettify"""

print(parsed)

