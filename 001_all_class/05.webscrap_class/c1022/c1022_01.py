import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

#print(res.text) #타입 str

#태그를 활용한 검색방법
# find, find_all,  == select_one, select 같다
soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("h2",{"class":"rankingnews_tit"}))
# print(soup.select_one("h2.rankingnews_tit").text)
#print(soup.select_one("div#header")) #아이디로 찾기


# #html,css 파싱이 되어서 깔끔하게  출력
# print(soup.prettify())

# ##언론사별랭킹 내가한거
# title = soup.select_one("strong.rankingnews_name")
# lists = soup.select_one("ul.rankingnews_list")
# print("언론사 : ",title.text)
# for list in lists:
#   print(list.select_one("li").a)

# # select_one,select 사용
# data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking")
# news = data.select_one("div.rankingnews_box")
# print("언론사 이름 : ",news.select_one("strong.rankingnews_name").text)
# news_lists = news.select("ul.rankingnews_list>li")
# for idx,news_list in enumerate(news_lists):
#   print(f"{idx+1} : ",news_list.select_one("div.list_content>a").text)


# # select_one,select 사용
# data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking")
# news_lists = data.select("div.rankingnews_box")
# print("개수 :",len(news_lists))
# for news in news_lists:
#   print("언론사 이름 : ",news.select_one("strong.rankingnews_name").text)
#   news_lists = news.select("ul.rankingnews_list>li")
#   for idx,news_list in enumerate(news_lists):
#     print(f"{idx+1} : ",news_list.select_one("div.list_content>a").text)
#   print("-"*50)