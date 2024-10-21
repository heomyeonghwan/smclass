# a = "안녕하세요. 빈깁습니다. 파이썬 수업입니다."

# #print(a.find("자바")) #없는거 -1
# search = "파이썬"
# print(a.find("search"))
# print(a[a.find(search):a.find(search)+3])


import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"class":"rankingnews_box"}))
# print(len(soup.find_all("div",{"class":"rankingnews_box"})))

# # find : 1개 검색
# rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"})
# # find_all : 여러개 검색
# rankingnews_boxs = rankingnews_wrap.find_all("div",{"class":"rankingnews_box"})
# print(len(rankingnews_boxs))

print(soup.title) ##제일먼저 찾아지는 것을 출력
print(soup.find("title")) ##특정위치의 태그를 출력
print(soup.find("div",{"class":"rankingnews_box_wrap"}))##특정위치의 태그와 속성을 가지고 찾아줌, 출력
newsLists = (soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"}))
print("여러개 개수 확인 :",len(newsLists)) # find_all : 여러개 검색 과 같음

for newsList in newsLists:
  print(newsList.find("strong",{"class":"rankingnews_name"}).text)