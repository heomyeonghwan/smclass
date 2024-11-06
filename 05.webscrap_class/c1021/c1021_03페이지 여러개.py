# naver 파일저장, 리솜리조트 파일저장
import requests
# url = [
#   "http://www.naver.com",
#   "https://www.resom.co.kr/resom/main/main.asp",
#   "http://www.daum.net/"
  
# ]

# headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
# for i in range(len(url)):
#   res = requests.get(url[i],headers=headers)
#   res.raise_for_status() #에러시 자동으로 종료

#   #파일저장
#   with open(f"c1021/{i}.html","w",encoding="utf-8") as f:
#     f.write(res.text)

# print("프로그램종료")


url = "http://www.daum.net/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 자동으로 종료
print(res.text)

with open(f"c1021/coupang.html","w",encoding="utf-8") as f:
  f.write(res.text)
