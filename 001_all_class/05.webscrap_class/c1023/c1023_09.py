# 다음 아이디, 패스워드 로그인
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# 1. 네이버항공권 페이지 열기
url = "https://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

# 2. 출발지 - 입력,김포