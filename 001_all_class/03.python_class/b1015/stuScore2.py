# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice =="1":
    while True:
      print("[학생성적입력]")
      no = stuNo+1
      stuNo+=1
      name = input(f"{no}학생의 이름을 입력.(0:이전페이지)>>")
      if name =="0":
        print("이전페이지로 이동")
        break
      score=[]
      total=0
      for i in range(3):
        k = int(input(f"{s_title[i+2]}성적입력.>>"))
        score.append(k)
        total += k
      avg = total/3
      rank = 0
      students.append({f"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank})
      print(f"{name} 학생성적이 저장되었습니다.")
      print()
      
  elif choice =="2":
    print("[학생성적출력]")
    print()
    for st in s_title:
      print(st,end="\t")
    print();print("-"*60)
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
  elif choice =="3":
    print("[학생성적수정]")
    name = input("찾고자하는 학생의 이름을 입력.>>")
    flag=0
    for s in students:
      if name ==s['name']:
        print(f"{name}학생을 찾았습니다.")
        print("[수정과목 선택]")
        print("1.국어성적")
        print("2.영어성적")
        print("3.수학성적")
        choice = int(input("원하는 항목번호를 입력.>>"))
        if choice == "1":
          print(f"현재 국어점수: {s['kor']}")
          s["kor"]=int(input("변경 국어점수: "))
        if choice == "2":
          print(f"현재 영어점수: {s['eng']}")
          s["eng"]=int(input("변경 영어점수: "))
        if choice == "3":
          print(f"현재 수학점수: {s['math']}")
          s["math"]=int(input("변경 수학점수: "))
        s["total"] = s["kor"]+s["eng"]+s["math"]
        s["avg"] = s["total"]/3
        print(f"{name} 학생의 성적이 수정되었습니다.")
        flag=1
    if flag ==0:
      print(f"{name} 학생이 존재하지 않습니다.")
    
  elif choice =="4":
    while True:
      print("[학생성적검색]")
      name = input("찾으시는 학생의 이름을 입력.>>")
      if name == "0":
        break
      for s in students:
        if s['name'] == name:
          for st in s_title:
            print(st,end="\t")
          print();print("-"*60)
          print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
          print()

    
  elif choice =="5":
    print("[학생성적삭제]")
    name = input("찾으시는 학생의 이름을 입력.>>")
    for s in students:
      if name == s["name"]:
        
  elif choice =="6":
   print("[등수입력]")
  elif choice =="7":
    pass
  elif choice =="0":
    pass
 