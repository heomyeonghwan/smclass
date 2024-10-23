# flight.html 금액이 50000원 미만 항공권을 출력
# 김포 -제주 80000원이하 항공권개수 : 15개
# 제주 -김포 80000원이하 항공권개수 : 30개
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

with open('flight.html','r',encoding='utf-8') as f:
  d