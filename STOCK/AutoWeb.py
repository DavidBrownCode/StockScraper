from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import requests
import webbrowser
import csv
import json
import datetime #import date
import os
import selenium

#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium import webdriver

#browser = webdriver.Chrome('\\Users\ASUS laptop\Desktop\DownloadsTemp\chromedriver_win32 (3)')with webdriver.Firefox() as driver:
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://twitter.com/login")

   # user name - #name = "session[username_or_email]"
   #password - name = "session[password]" or type = "password"
   #login button = <div aria-haspopup="false" disabled="" role="button" aria-disabled="true" class="css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-vlx1xi r-zg41ew r-1jayybb r-17bavie r-icoktb r-15bsvpr r-o7ynqc r-6416eg r-lrvibr" data-testid="LoginForm_Login_Button"><div dir="auto" class="css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-vw2c0b r-1777fci r-eljoum r-dnmrzs r-bcqeeo r-q4m81j r-qvutc0"><span class="css-901oao css-16my406 css-bfa6kz r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Log in</span></span></div></div>