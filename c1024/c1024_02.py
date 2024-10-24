#지마켓
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options

#selenium 숨김처리
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")


# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# browser.get(url)

# soup = BeautifulSoup(browser.page_source,"lxml")
# data = soup.select_one("#detected_value").text
# print(data)
# browser.get_screenshot_as_file("gmarket.png") #화면캡쳐


#노트북을 검색한 사이트 1,2,3페이지에서
#만족도가 95이상이면서 금액은 150만원 이하
#평가수가 100이상을 검색
#파일저장
for i in range(3):
  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i+1}"
  browser = webdriver.Chrome(options=options)
  browser.maximize_window()
  browser.get(url)
  time.sleep(3)

  soup = BeautifulSoup(browser.page_source,"lxml")
  browser.get_screenshot_as_file("gmarket.png") #화면캡쳐
  with open(f'c1024/gmarket{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())


#파일불러오기
for i in range(3):
  with open(f'c1024/gmarket{i+1}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,"lxml")
    


input("Enter키를 입력하면 완료됩니다.")
