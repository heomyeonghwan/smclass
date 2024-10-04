students= []
no=1
s_title= ['번호','이름','국어','영어','수학','합계','평균','등수']

#학생성적프로그램
print("[학생성적프로그램]")
print("-"*60)
print("1. 학생성적입력")
print("2. 학생성적출력")
print("3. 학생성적수정")
print("4. 학생성적검색")
print("0. 프로그램종료")
print("-"*60)
choice = input("원하는 번호를 입력하세요(종료:0).>>")

if choice =='1':
  print("[학생성적입력]")
  while True:
    name = input(f"{no}번째 이름을 입력하세요(상위이동:0)")
    if name =='0':
      print("메뉴화면으로 이동합니다.")
      break
    kor = int(input("국어성적을 입력하세요"))
    eng = int(input("영어성적을 입력하세요"))
    math = int(input("수학성적을 입력하세요"))
    total = kor+eng+math
    avg = total/3
    rank = 0
    s=[no,name,kor,eng,math,total,avg,rank]
    students.append(s)
    print(f"{no},{name},{kor},{eng},{math},\
          {total},{avg},{rank:.2f}")
    no+=1

elif choice =='2':
  print("[학생성적출력]")
  print()

  
  for s in s_title:
    print(s,end="\t")
  print()
  print("-"*60)

  for s in students:
    print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
  print()
elif choice =='3':
  print("[학생성적수정]")

elif choice =='4':
  print("[학생성적검색]")
  name = input("찾고자하는 학생 이름을 입력하세요.>>")
  #students 에서 검색
  count=0
  for s in students:
    if s[1] == name:
      print(f"{name} 학생을 찾았습니다.")
      #c찾은학생의 데이터를 출력
      
      #상단출력
      for st in s_title:
        print(s,end="\t")
      print(); print("-"*60)

      #학생성적 출력
      for s in students:
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print()
        count=1
        break
  if(count==0):
    print("찾고자하는 학생이름이없습니다.")
      
elif choice =='0':
  print("[프로그램종료]")
  print("프로그램을 종료합니다.")

 
  

  