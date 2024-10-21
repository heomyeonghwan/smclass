students= []
no=1
s_title= ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
  #학생성적프로그램
  print("[학생성적프로그램]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요(종료:0).>>")

  if choice == "1":
    print("[학생성적입력]")
    while True:
      name = input(f"{no}번째 학생이름을 입력하세요(상위이동:0)")
      if name =="0":
        print("메뉴화면으로 이동합니다.")
        break
      kor = int(input("국어성적을 입력하세요"))
      eng = int(input("영어성적을 입력하세요"))
      math = int(input("수학성적을 입력하세요"))
      total = kor+eng+math
      avg = total/3
      rank = 0

      print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{avg:.2f},등수:{rank}")
      s=[no,name,kor,eng,math,total,avg,rank]
      students.append(s)
      no +=1
  elif choice =="2":
    print("[학생성적출력]")
    print()
    for st in s_title:
      print(st,end="\t")
      print()
      print("-"*60)
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print()
  elif choice =="3":
    print("[학생성적수정]")
    name = print("수정하고자하는 학생이름을 입력하세요")
    count = 0
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        print("[과목선택]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("0. 수정취소")
        choice = input("원하는 번호를 입력하세요.")
        if choice == "1":
          print("현재 국어점수:",s[2])
          s[2]=int(input("변경 국어점수 입력: "))
        elif choice == "1":
          print("현재 국어점수:",s[3])
          s[3]=int(input("변경 국어점수 입력: "))
        elif choice == "1":
          print("현재 국어점수:",s[4])
          s[4]=int(input("변경 국어점수 입력: "))
        elif choice == "0":
          print("성적수정을 취소합니다.")
        if choice != "0":
          s[5]=s[2]+s[3]+s[4]
          s[6]=s[5]/3
          print(f"{name}학생의 성적이 변경되었습니다.")
          count=1
    if count == 0:
      print("수정하고자하는 학생이름이 없습니다.")
      
        
          
  elif choice =="4":
    print("[학생성적검색]")
    name = input("찾고자하는 학생이름을 입력하세요.")
    count = 0
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        for st in s_title:
          print(st,end="\t")
        print(); print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}")
        count=1
        break
    if(count==0):
      print("찾고자하는 학생이 없습니다.")
      print()

  elif choice =="0":
    print("[성적처리 프로그램종료]")
    print("프로그램을 종료합니다")
    break
  
