students=[]
no = 1
count = 0
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
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
    print("[학생성적입력]")
    while True:
      name = input(f"{no}번째 학생의 이름을 입력하세요.(상위이동:0)>>")
      if name =="0":
        print("상위메뉴로 이동합니다.")
        break
      kor = int(input("국어점수를 입력하세요.")) 
      eng = int(input("영어점수를 입력하세요.")) 
      math= int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      students.append([no,name,kor,eng,math,total,avg,rank])
      print(f"{name} 학생의 성적이 저장되었습니다.")
      no+=1

  elif choice == "2":
    print("[학생성적출력]")
    print()
    for st in s_title:
      print(st,end="\t")
    print()
    print("-"*60)
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
    print()
  
  elif choice == "3":
    print("[ 학생성적 수정 ]")
    name = input("수정할 학생의 이름을 입력하세요.>>")
    count=0
    for s in students:
      if s[1] == name:
        print(f"{name}의 성적을 찾았습니다.")
        print("[수정할 과목선택]")
        print("1. 국어성적")
        print("2. 영어성적")
        print("3. 수학성적")
        print("0. 수정취소")
        choice = input("수정할 과목의 번호를 입력해주세요.>>")
        if choice =="1":
          print("저장된 국어점수:",s[2])
          s[2]= int(input("변경될 국어점수 입력 >> "))
        elif choice =="2":
          print("저장된 국어점수:",s[3])
          s[3]= int(input("변경될 영어점수 입력 >> "))
        elif choice =="3":
          print("저장된 국어점수:",s[4])
          s[4]= int(input("변경될 수학점수 입력 >> "))
        elif choice =="0":
          print("성적수정을 취소합니다")
          count=1
        if choice !="0":
          s[5]=s[2]+s[3]+s[4]
          s[6]=s[5]/3
          print(f"{name} 학생의 성적이 변경되었습니다.")
          count=1
    if count==0:
      print(f"{name} 학생이 존재하지않습니다.")
      print()

  elif choice == "4":
    print("[학생성적검색]")
    name = input("찾으시는 학생의 이름을 입력하세요.>>")
    count=0
    for s in students:
      if s[1] == name:
        print(f"{name}의 성적을 찾았습니다.")
        for st in s_title:
          print(st,end="\t")
        print()
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
        print()
        count=1
        break
    if count==0:
      print(f"{name} 학생이 존재하지않습니다.")
      print()
                 
  elif choice == "5":
    print("[학생성적 삭제]")
    name = input("찾으시는 학생의 이름을 입력하세요.>>")
  elif choice == "6":
    pass
  elif choice == "0":
    print("[프로그램 종료]")
    print("프로그램을 종료합니다.")
    break