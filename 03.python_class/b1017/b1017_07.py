#members 리스트에 딕셔너리 저장
members = []
m_keys = ['id','pw','name','nicName','address','money']

#아이디 검색
#members 리스트에서
#입력한 문자로 검색된 데이터를 모두 출력하시오
# (a 가 들어가 있는 아이디를  출력)


#파일불러오기
f = open('b1017/member.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  #m리스트 저장
  m = line.strip().split(",")
  m[5] = int(m[5]) #money
  #members 리스트에 딕셔너리 저장
  members.append(dict(zip(m_keys,m)))
f.close()
# #회원검색
# search = input("검색할 회원이름을 입력>>")
# flag=0
# mm = []
# for m in members:
#   if m['id'].find(search) != -1:
#     print("검색 회원을 찾았습니다.")
#     mm.append(m)
#     flag=1
# if flag ==0:
#   print("검색한회원이 없음")
# else:
#   print("총검색된 인원:",len(mm))
#   print(mm)

while True:
  print("1. 회원등록")
  print("2. 회원검색")
  choice = input("원하는 번호를 입력")
  if choice == "1":
    id = input("ID를 입력하세요")
    flag=0
    for m in members:
      if m['id'] == id:
        print(f"{id}과 동일한 아이디가 있습니다. 다시입력하세요.")
        flag=1
        break
    if flag ==1:
      continue
    else:
      print(f"{id}은(는) 사용가능합니다")
      print()
    pw = input("PW를 입력하세요")
    name = input("이름을 입력하세요")
    nicName = input("닉네임을 입력하세요")
    money = int(input("충전금액을 입력하세요"))
    address = input("주소를 입력하세요")
    m_list=[id,pw,name,nicName,address,money]
    members.append(dict(zip(m_keys,m_list)))
    print(f"{id} 님 회원가입이 완료되었습니다")
    print(m_list)
    print("-"*60)
    print(members)

  elif choice == "2":
    #회원검색
    search = input("검색할 회원이름을 입력>>")
    flag=0
    mm = []
    for m in members:
      if m['id'].find(search) != -1:
        print("검색 회원을 찾았습니다.")
        mm.append(m)
        flag=1
    if flag ==0:
      print("검색한회원이 없음")
    else:
      print("총검색된 인원:",len(mm))
      print(mm)



