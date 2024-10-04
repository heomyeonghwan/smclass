students = []
no = 1
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
# 학생성적프로그램
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice =="1":
    print("[학생성적 입력]")
    while True:
      name = input(f"{no}번쨰 이름을 입력하세요.(상위이동 : 0)")
      if name =="0":
        print("메뉴화면으로 이동합니다.")
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      s = [no,name,kor,eng,math,total,avg,rank]
      students.append(s)
      print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{avg:.2f},등수:{rank}")
      no+=1
  elif choice =="2":
    print("[학생성적 출력]")
    print()
    for st in s_title:  #상단
      print(st,end="\t")
    print()
    print("-"*60)
    for s in students: #성적출력
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print()
  elif choice =="3":
    print("[학생성적 수정]")


  elif choice =="4":
    print("[학생성적 검색]")
    name = input("찾고자 하는 학생이름을입력하세요.>>")
    count =0
    for s in students: # students에서 검색
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        for st in s_title: #상단
          print(st,end="\t")
        print()
        print("-*60")
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print()
        count = 1
        break
    if count == 0:
      print("찾고자 하는 학생이름이 없습니다.")
      print()

  elif choice =="5":
    print("[학생성적 삭제]")
  elif choice =="6":
    print("[등수처리]")
  elif choice =="0":
    print("[프로그램 종료]")
    print("성적처리 프로그램을 종료합니다.")
    break