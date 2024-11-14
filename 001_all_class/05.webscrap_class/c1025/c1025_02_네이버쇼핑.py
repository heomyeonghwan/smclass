#
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

#제목, 금액, 평점, 평가수, 찜 정보를 1~5페이지 까지 가져와서
#평점4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장 후 출력
#네이버에서 검색창 입력 네이버 쇼핑 클릭 네이버쇼핑에서 무선마우스 입력

#파일저장
browser = webdriver.Chrome()
browser.maximize_window()
for i in range(5):
  url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i+1}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
  browser.get(url)
  time.sleep(2)
  # 화면 스크롤해서 내리기 반복
  prev_height = browser.execute_script("return document.body.scrollHeight")
  while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
      break
    prev_height = curr_height

  soup = BeautifulSoup(browser.page_source,'lxml')
  with open(f'c1025/naver_shop{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
    break

for i in range(5):
  with open(f'c1025/naver_shop{i+1}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,"lxml")

    data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx>div")
    s_lists = data.select(".product_item__MDtDF") 
    lists = data.select(".adProduct_item__1zC9h") 
    for idx,s_list in s_lists:
      print("제목:",s_list.select("a").text.strip())
      print

    break

input("엔터키를 누르면 종료")