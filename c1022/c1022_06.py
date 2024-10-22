# title = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']

# a = ','.join(title)+"\n"
# print(a)
# with open('c1022/a.txt','w',encoding='utf-8') as f:
#   f.write(a)

import requests
from bs4 import BeautifulSoup
url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text,"lxml") 
#print(soup.prettify())

#순위,사진링크주소,제목, 가수명 
#타이틀 출력



#순위,사진링크주소,제목, 가수명  #내가
data = soup.select_one("#frm > div > table > tbody")
print("순위 : ",data.select_one("span.rank").text)
print("사진링크주소 : ",data.select_one("#lst50 > td:nth-child(4) > div > a>img").get("src"))
print("제목:",data.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a").text)
print("가수명:",data.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a:nth-child(1)").text)

pops = data.select("tbody>tr")
for pop in pops:
  print("순위 : ",pop.select_one("span.rank").text)
  print("사진링크주소 : ",pop.select_one("#lst50 > td:nth-child(4) > div > a>img").get("src"))
  print("제목:",pop.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a").text)
  print("가수명:",pop.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a:nth-child(1)").text)
