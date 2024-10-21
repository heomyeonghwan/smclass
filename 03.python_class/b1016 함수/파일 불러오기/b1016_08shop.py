#smshop
# 1.member 파일 읽어와서 member 딕셔너리 저장
# 2. cart파일 읽고 , cart 저장
# product 만들기
# 프로그램 시작(로그인 화면)
# 3. 화면구현(상품 화면)
# 3-1 상품구매


#1.날짜
import datetime
#member 리스트
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
f.close()
#cart 리스트
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
f.close()
#상품 리스트
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
#아이디비번입력받기
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
if choice ==1: #def buy()-함수로 뺄때 리턴값주기
  print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  print()
  #카트에 담기(딕셔너리로),카트번호 1개씩오르게하기
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:$S")
  c = {"cno":cartNo+1,"id":section_info['id'],"name":section_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  cart.append(c)
  cartNo += 1
  #금액차감
  section_info['money'] -= product[choice-1]['price']
  
elif choice ==2:
  print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  print()
  #카트에 담기(딕셔너리로),카트번호 1개씩오르게하기
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:$S")
  c = {"cno":cartNo+1,"id":section_info['id'],"name":section_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  cart.append(c)
  cartNo += 1
  #금액차감
  section_info['money'] -= product[choice-1]['price']
elif choice ==3:
  print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  print()
  #카트에 담기(딕셔너리로),카트번호 1개씩오르게하기
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:$S")
  c = {"cno":cartNo+1,"id":section_info['id'],"name":section_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  cart.append(c)
  cartNo += 1
  #금액차감
  section_info['money'] -= product[choice-1]['price']
elif choice ==4:
  print(f"{product[choice-1]['pName']}를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  print()
  #카트에 담기(딕셔너리로),카트번호 1개씩오르게하기
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:$S")
  c = {"cno":cartNo+1,"id":section_info['id'],"name":section_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  cart.append(c)
  cartNo += 1
  #금액차감
  section_info['money'] -= product[choice-1]['price']
elif choice ==7:# 내용저장 def buy_save()
  ##멤버 파일로 저장
  # member.txt 파일생성해서 csv형태로 문자열로 써서 저장하시오.
  f = open('member.txt','w',encoding='utf-8')
  for m in member:
    f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['address']},{m['money']}\n")
  f.close
  ##카트 파일로 저장
  # cart.txt 파일생성해서 csv형태로 문자열로 저장하시오.
  f = open('cart.txt','w',encoding='utf-8')
  for c in cart:
    f.write(f"{c['cno']},{c['id']},{c['name']},{c['pCode']},{c['pName']},{c['price']},{c['date']}\n")
  f.close()
  print("내용저장이 완료되었습니다.")
  print()

elif choice ==8: #구매내역 def buy_output()
# 구매내역출력

  #상단출력
  print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:14s}\t{p_title[5]}\t{p_title[6]}")
  print("-"*85)
  #하단출력 및 총 구매금액, 구매건수
  sum=0
  for c in cart:
    sum += c['price']
    print(f"{c['cno']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:14s}\t{c['price']}\t{c['date']}")
  print(f"총 구매 금액 : {sum:,}")
  print(f"총 구매 건수 : {len(cart)}")
 
  
elif choice ==9: #금액충전 def buy_money()
  # 금액충전 / 현재금액에 충전금액더하기
  print("[ 금액충전 ]")
  print(f"현재 금액 : {section_info['money']}")
  input_money = int(input("원하는 금액을 입력하세요.>> "))
  section_info['money'] += input_money
  print(f"충전된 금액 : {section_info['money']}")