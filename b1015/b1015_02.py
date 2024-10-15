
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

#학생성적입력 함수선언
def stu_input(stuNo,students):
  #global stuNo
  while True:
    print("[학생성적입력]")
    no = stuNo+1
    name = input(f"{no}번재 학생이름을 입력(0:이전화면 이동)")
    if name == "0":
      print("이전화면으로 이동합니다.")
      print()
      break

    score = []
    total = 0
    for i in range(3):
      k = int(input(f"{s_title[i+2]}점수를 입력>>"))
      total += k
      score.append(k)

    avg = total/3
    rank = 0
    stuNo += 1

    s={"no":no,"name":name,"kor":s_title[2],"eng":s_title[3],"math":s_title[4],"total":total,"avg":avg,"rank":rank}
    students.append(s)
    print(f"{name}학생의 성적이 저장되었습니다.")
    print()

    print(students)
  return stuNo

#####프로그램 시작
choice = input("원하는 항목번호 입력>>")

if choice =="1":
  stuNo = stu_input(stuNo,students)
  print("현재 학생번호:",stuNo)
  print(students)