# a = "123,000"
# b = "1,000"
# print(a+b)

# print(int(a.replace(",",""))+int(b.replace(",","")))#쉼표를 빈문자열로

import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text,"lxml")
#기준점
data = soup.select_one("#contentarea > div.box_type_l > table")
#상단타이틀
tits = data.select("tr.type1>th")
#타이틀 출력
for tit in tits:
  print(tit.text,end="\t")
print(); print("-"*100)

#하단 주식 30개
stocks = data.select("tr")
print("개수 : ",len(stocks))
