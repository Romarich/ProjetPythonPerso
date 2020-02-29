from tkinter import *
import urllib
import urllib3
from PIL import Image, ImageTk
import requests
import json
import time
from bs4 import BeautifulSoup

#http = urllib3.PoolManager()
#url = 'http://www.thefamouspeople.com/singers.php'
#response = http.request('GET', url)
#soup = BeautifulSoup(response.data)
#ou 
#curl



http = urllib3.PoolManager()
url = 'https://www.tradingview.com/x/Hmrc5gN2/'
response = http.request('GET', url)
soup = BeautifulSoup(response.data)

print(soup)
