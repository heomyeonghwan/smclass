#클래스 생성
class Student:
  # #1. 생성자 정의가 없음
  # #기본생성자
  
  # no = 0
  # name = ""
  # kor = 0
  # eng = 0
  # math = 0
  # total = 0
  # avg = 0
  # rank = 0

  
  def __init__(self,no): 
    self.no = no #인스턴스변수 > 참조변수.변수명, 참조변수.함수명


#---------------------------
1 = Student() ##객체선언
# s1 = Student() ##객체선언
# s1.no = 1
# s1.name = "홍길동"
# print(s1) # 클래스값만으로는 주소값만 출력
# print(s1.name) #변수명까지 넣어야 출력

s2 =Student(2)# 생성자 정의가 있어야 출력
print(s2.no) 



