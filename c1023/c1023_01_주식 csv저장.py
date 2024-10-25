import os
import requests
from bs4 import BeautifulSoup
import time
import csv
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

#데이터 가져오기
soup = BeautifulSoup(res.text,"lxml") 
print(soup.prettify()) 

#기준점
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
#print(len(stocks)) #개수확인


# #1.상단타이틀 만들기
f = open('c1023/stock.csv','w',encoding='utf-8-sig',newline='')
writer = csv.writer(f)

# #list 생성(2)/리스트 내포
# sts = stocks[0].select("th")
# st_list = [st.text for st in sts]
# print(st_list)
##
st_list = [st.text for st in stocks[0].select("th")]
#print(st_list)
#print(len(st_list)) #상단타이틀 항목 : 12개

writer.writerow(st_list)

#30개 주식정보를 csv파일로 저장하시오
print(len(stocks)) # 50개
for stock in stocks:
  sts = stock.select("td")
  if len(sts) <= 1: continue #td갯수
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  writer.writerow(sto_list) #writerow 리스트타입저장
f.close()
print("완료")

# #2. 
# #print(stocks[1].select("td")) 
# sto_list = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[2].select("td")]
# print(sto_list)



# #list 생성(1)
# sts = stocks[0].select("th")
# st_list = []
# for st in sts:
#   print(st.text)
#   st_list.append(st.text)
# print(st_list)