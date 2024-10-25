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

url = "http://www.naver.com"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
#네이버쇼핑 클릭
elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[4]/a').click()
time.sleep(1)
#
# 새로운 탭으로 이동
browser.switch_to.window(browser.window_handles[1])
elem = browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
elem.click()
time.sleep(2)
elem.send_keys("무선마우스")
elem.send_keys(Keys.ENTER)









input("엔터키를 누르면 종료")