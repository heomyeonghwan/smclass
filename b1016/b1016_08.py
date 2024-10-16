#smshop
# 1.member 파일 읽어와서 member 딕셔너리 저장
# 2. cart파일 읽고 , cart 저장
# product 만들기
# 프로그램 시작(로그인 화면)
# 3. 화면구현(상품 화면)
# 3-1 상품구매

import datetime
#-----member.txt파일 읽기, 딕셔너리로 저장
member = []
m_keys = ['id','pw','name','nicName','address','money']

f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  m = line.strip().split(",")
  m[5] = int(m[5])
  member.append(dict(zip(m_keys,m)))
print(member)

#-------cart파일 읽고 cart 딕셔너리 저장
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]

f = open('cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line : break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))

#product,session_info,p_title
product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]
section_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]

#--------------프로그램시작
#로그인 화면
while True:
  print("[ 로그인 화면 ]")
  input_id = input("아이디를 입력.>>")
  input_pw = input("비밀번호를 입력.>>")
#아이디 비번 일치 확인
  flag = 0
  for m in member:
    if input_id == m['id'] and input_pw == m['pw']:
      print("SM SHOP에 오신것을 환영합니다.! ")
      section_info = m
      flag = 1
      break
  if flag == 0:
    print("아이디 또는 패스워드가 일치하지 않습니다.")
  else:
    break
#메인 화면
print("[SM-SHOP]")
print(f"닉네임 : {section_info['nicName']}님")
print(f"사용가능금액 : {section_info['money']}원")
print("1. 삼성TV - 2,000,000")
print("2. LG냉장고 - 3,000,000")
print("3. 스피커 - 500,000")
print("4. 세탁기 - 1,000,000")
print("7. 내용저장")
print("8. 구매내역 ")
print("9. 금액충전 ")
choice = int(input("구매하려는 상품의 번호를 입력하세요.>>"))
if choice ==1:
  print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  print()
  