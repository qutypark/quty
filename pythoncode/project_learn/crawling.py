# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:18:53 2021

"""

from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPProxyAuth
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml.html as lh

proxies = {'http': 'http://user:pw@ip:port',
           'https':'https://user:pw@ip:port'}

payload={'loginId':'id','password':'pw'}

session = requests.Session()

# login
s = session.post("url/login",proxies=proxies,data=payload)

# go to content page
s = session.get("rul/content",proxies=proxies)
soup = BeautifulSoup(s.content, "html.parser")

float_right = soup.find('div', attrs={'class':'float-right'})

name = name_box.text.strip() 

results = soup.find('td', class_='head number')
