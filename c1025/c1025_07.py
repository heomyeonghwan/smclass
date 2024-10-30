from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

soup = BeautifulSoup(browser.page_source,'lxml')
with open(f'c1025/1.txt','w',encoding='utf-8') as f:
  f.write(soup.prettify())


  