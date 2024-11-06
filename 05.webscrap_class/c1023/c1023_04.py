# import time
# import random
# # print(random.uniform(1,3))#uniform 실수
# # print(random.randint(1,3))

# # #
# # a =[0]*100
# # for i in range(100):
# #   a[i] = i

# # # 똑같음
# b= [i for i in range(100)]
# #print(b)

# for i in b:
#   print(i)
#   time.sleep(random.uniform(1,3))


#다음사이트에서 검색창에 주식정보 입력해서 페이지 이동을 하시오
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://daum.net")

elem = browser.find_element(By.ID,'q')
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)

browser.get("http://naver.com")
elem = browser.find_element(By.CLASS_NAME,'search_input')
elem.send_keys("주식정보")
time.sleep(3)
elem.send_keys(Keys.ENTER)

time.sleep(100)