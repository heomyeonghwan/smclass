import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
#print(soup.prettify())

# 제목,금액,평점,평가수,링크주소,이미지주소
# 기준점
data = soup.select_one("#productList")
# #1개
lists = data.select("li")
# print("1. 링크주소 :","https://www.coupang.com"+lists[0].select_one("a")['href'])
# print("2. 제목 :",lists[0].select_one("div.name").text)
# price = int(lists[0].select_one("strong.price-value").text.replace(",",""))
# print("3. 금액 :",price)
# rating = float(lists[0].select_one("em.rating").text)
# print("4. 평점 :",rating)
# num = int(lists[0].select_one("span.rating-total-count").text[1:-1])
# print("5. 평가수 :",num)
# print("6. 이미지 :","https:/"+lists[0].select_one("dt.image>img")['src'][1:])


#금액이 :90만원이상 평점은 4.5 이상 평가수 100명이상
lists = data.select("li")
n_lists = []
for idx,list in enumerate(lists):
  n_list = [] #제목,금액 평점 평가수 링크 이미지
  try:
    #pric,rating,num 타입 변경
    price = int(lists[0].select_one("strong.price-value").text.replace(",",""))
    rating = float(lists[0].select_one("em.rating").text)
    num = int(lists[0].select_one("span.rating-total-count").text[1:-1])
    #금액,평점,평가수 비교
    if price >=900000 and rating>=4.5 and num >=500:
      print(f"[{idx} 번째]")
      print("1. 링크주소 :","https://www.coupang.com"+lists[0].select_one("a")['href'])
      print("2. 제목 :",lists[0].select_one("div.name").text)
      print("3. 금액 :",price)
      print("4. 평점 :",rating)
      print("5. 평가수 :",num)
      print("6. 이미지 :","https:/"+lists[0].select_one("dt.image>img")['src'][1:])
    else:
      print(f"[{idx}번째] : 제외")
  except Exception as e:
    print(f"{idx}:에러",e)


  while True:
    print("[노트북비교]")
    print("1. 금액정렬")
    print("2. 금액역순정렬")
    print("3. 평점정렬")
    print("4. 평점역순정렬")
    print("0. 종료")
    print("-"*50)
    choice = input("원하는 번호를 입력>>>")

    if choice == "1":
      pass
    elif choice == "2":
      pass
    elif choice == "3":
      pass
    elif choice == "4":
      pass
    elif choice == "0":
      pass