#웹 스크래핑 세팅


#requests로 정보를 가져올시 
# 제이퀘리 자바스크립트 외부페이지 react,vue.. 비동기식으로 작동되는 소스는 가져오지 못함 

import requests
#res = requests.get("https://www.google.com/") #html 소스를 가져옴
res = requests.get("https://www.naver.com/") #html 소스를 가져옴
#res = requests.get("https://www.melon.com/index.htm/") #html 소스를 가져옴
#res.raise_for_status() #에러시 자동으로 종료
print("응답코드:",res.status_code) # 200
#print(res.text) #html소스 출력

print("총 문자길이:",len(res.text))

# #res.raise_for_status()를 안쓰고 에러 확인
# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할수없습니다.")

# # 웹 소스 코드 파일저장
# f = open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()

#f.close() 를 안해도 자동으로 닫힘
with open("c1021/naver.html","w",encoding="utf-8") as f:
  f.write(res.text)
