#Student 클래스 생성후 
# 데이터를 직접입력 받아, 클래스 선언 후 저장
# 번호 자동부여, 이름 국어 영어수학 합계 평균 등수
# 클래스 전체출력
# 클래스 수정
#_--------------------------------------
#클래스 생성
class Student:
  count = 0
  students = []
  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    #클래스 리스트에 추가
    Student.students.append(self)
  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"
  # def print(self): #딕셔너리 타입으로 리턴
  #   return {"no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,"math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank}

#[학생성적프로그램]
#1.학생성적입력
#2.학생성적출력
#3.학생성적수정
while True:
  print("[학생성적프로그램]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  choice = int(input("항목번호 입력>>"))
  if choice == 1:
    print("[학생성적입력]")
    name = input("이름을 입력>>")
    kor = int(input("국어성적>>"))
    eng = int(input("영어성적>>"))
    math = int(input("수학성적>>"))
    #객체선언
    s1 = Student(name,kor,eng,math)

    for s in Student.students:
      print(s)