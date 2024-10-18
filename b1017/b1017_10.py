import datetime
import os
members = []
m_title = ['id','pw','name','nicName','address','money']
#### member.csv파일 불러오기
f = open('b1017/member.csv',"r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  # c리스트 저장
  c = line.strip().split(",")
  c[5] = int(c[5])  # money
  # members리스트에 딕셔너리 저장
  members.append(dict(zip(m_title,c)))
f.close()
#-----------------------------
# cart.txt파일 읽기, member딕셔너리 저장
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]
# isfile : 파일인지확인, isdir : 디렉토리인지 확인, exists : 파일이 존재하는지 확인
if os.path.exists("b1017/cart.txt"):
  f = open('b1017/cart.txt','r',encoding='utf-8')
  while True:
    line = f.readline()
    if not line: break
    c = line.strip().split(",")
    c[0] = int(c[0])
    c[5] = int(c[5])
    cart.append(dict(zip(c_keys,c)))
  f.close()
#-----------------------------------------
# 파일 저장해서 불러오기
product = [
  # {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  # {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  # {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  # {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]


#-------------------------------------------------------------------------------
session_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]
#####  프로그램 시작  #####
while True:
  print("[ 메인화면 ]")
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>>")
  if choice == "1":
    # 프로그램 구현
    input_id = input("아이디를 입력하세요.>> ")
    input_pw = input("패스워드를 입력하세요.>> ")
    flag = 0
    for m in members:
      if input_id == m['id'] and input_pw == m['pw']:
        print("SM SHOP에 오신것을 환영합니다.! ")
        session_info = m
        flag = 1
        break  # for반복문
    if flag == 0:
      print("아이디 또는 패스워드가 일치하지 않습니다.!")
    else:
      break
  elif choice == "2":
    id = input("ID를 입력하세요")
    flag=0
    for m in members:
      if m['id']==id:
        print(f"{id}와 동일한 아이디가 있습니다. 다시입력해주세요")
        flag=1
        break
    if flag ==0:
      print(f"{id}는 사용가능합니다.")
      print()
    pw = input("PW를 입력하세요")
    name = input("이름을 입력하세요")
    nicName = input("닉네임을 입력하세요")
    address = input("주소를 입력하세요")
    money = int(input("충전금액을 입력하세요"))
    m_list=[id,pw,name,nicName,address,money]
    members.append(dict(zip(m_title,m_list)))
    print(f"{id} 님 회원가입이 완료되었습니다")
    print(m_list)
    print("-"*60)
    print(members)
    
    # 프로그램 구현


  elif choice == "0":
    print("프로그램을 종료합니다.")
    break
# 프로그램을 구현하시오.
while True:
  print("           [ SM-SHOP ]")
  print(f"                       닉네임:{session_info['nicName']}님")
  print(f"                       금액 :{session_info['money']:,} 원")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역 ")
  print("9. 금액충전 ")
  choice = int(input("구매하려는 상품번호를 입력하세요.>> "))
  # 프로그램 구현
  if choice == 1:
    print(f"{product[choice-1]['pName']} 를 구매하셨습니다.")
    print("구매내역에 등록합니다.")
    print()
    # 로그인정보 - session_info
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    c = {"cno":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
    session_info['money'] -= product[choice-1]['price']
    cart.append(c)
    cartNo += 1
    
  elif choice == 2:
    print(f"{product[choice-1]['pName']} 를 구매하셨습니다.")
    print("구매내역에 등록합니다.")
    print()
    # 로그인정보 - session_info
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    c = {"cno":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
    session_info['money'] -= product[choice-1]['price']
    cart.append(c)
    cartNo += 1   
  elif choice == 3:
    print(f"{product[choice-1]['pName']} 를 구매하셨습니다.")
    print("구매내역에 등록합니다.")
    print()
    # 로그인정보 - session_info
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    c = {"cno":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
    session_info['money'] -= product[choice-1]['price']
    cart.append(c)
    cartNo += 1    
  elif choice == 4:
    print(f"{product[choice-1]['pName']} 를 구매하셨습니다.")
    print("구매내역에 등록합니다.")
    print()
    # 로그인정보 - session_info
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    c = {"cno":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
    session_info['money'] -= product[choice-1]['price']
    cart.append(c)
    cartNo += 1   
  elif choice == 7:
    # member.txt 파일생성해서 csv형태로 문자열로 저장하시오.
    f = open('member.txt','w',encoding='utf-8')
    for m in members:
      f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['address']},{m['money']}\n")
    f.close()
    # cart.txt 파일생성해서 csv형태로 문자열로 저장하시오.
    f = open('cart.txt','w',encoding='utf-8')
    for c in cart:
      f.write(f"{c['cno']},{c['id']},{c['name']},{c['pCode']},{c['pName']},{c['price']},{c['date']}\n")
    f.close()
    print("내용저장이 완료되었습니다.")
    print()                  
  elif choice == 8:
    # 구매내역 출력
    print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:14s}\t{p_title[5]}\t{p_title[6]}")
    print("-"*85)
    sum = 0
    for c in cart:
      sum += c['price']
      print(f"{c['cno']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:14s}\t{c['price']}\t{c['date']}")
    print(f"총 구매 금액 : {sum:,}")
    print(f"총 구매 건수 : {len(cart)}")
  elif choice == 9:
    # 금액충전
    print("[ 금액충전 ]")
    print(f"현재 금액 : {session_info['money']}")
    input_money = int(input("원하는 금액을 입력하세요.>> "))
    session_info['money'] += input_money
    print(f"충전된 금액 : {session_info['money']}")