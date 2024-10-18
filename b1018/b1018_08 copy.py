  #변수2종류-  
  # 지역변수 : 함수내에 선언된 변수,함수가 종료되면 사라짐
  # 인스턴스변수 - self/  객체선언시 만들어짐,각각의 객체마다 변수가 생성됨
  # - 참조변수명.변수명
  # 클래스 변수- 객체선언하지 않아도 만들어짐, 모든객체가 공통으로 사용
  # -클래스명.변수명
  #함수 2종류
  #인스턴스 함수 - 객체선언할때 만들어짐 , 각각의 객체마다 함수가 생성됨
  # - 참조변수명.함수명
  #클래스 함수 - 객체선언하지 않아도 만들어짐, 모든객체가 공통으로 사용
  # -클래스명.함수명 / @classmethod #클래스 함수표시

  # __str__
  #객체선언 한 참조변수를 출력하면 > 주소값이 출력됨
  # 참조변수를 출력해서 원하는 데이터를 출력하려면, __str__함수를 사용한다
  #리턴값 : 문자열이어야한다

#클래스 생성
class Student:
  # #1. 생성자 정의가 없음
  # #기본생성자
  #kor = 100 #클래스변수 - 클래스명.변수명
  count = 1 #클래스 변수
  students=[]

  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math): ##클래스내에서만 쓰는 특별한함수( __##__)
    self.no = Student.count #클래스변수 -클래스명.변수명
    self.name = name  #인스턴스 변수- 참조변수명.변수명
    self.kor = kor  #인스턴스 변수
    self.eng = eng  #인스턴스 변수
    self.math = math  #인스턴스 변수
    Student.count += 1
    Student.students.append(self)


  def __str__(self):
    return f'{self.no},{self.name},{self.kor},{self.eng},{self.math}' #리턴값 : 문자열이어야한다


  #no getter를 사용하지 않으면 접근불가
  def get_no(self):
    return self.no
  
  def set_no(self,no):
    if no<0:raise "0이하는 입력을 할 수없습니다."
    self.no = no
  

s1 = Student("홍이",100,100,100)
print(s1)
s2 = Student("유관",100,100,90)
print(s2)
s3 = Student("김구",100,100,80)
print(s3)
s4 = Student("길동",100,100,70)
print(s4)
print("-"*50)
#클래스 __str__
Student.stu_print()
#student



# s1 = Student()
# #s1.no = -100
# s1.set_no(100)
# print(s1.get_no())

    
# #객체선언 - 참조변수명 = 클래스명()
# #
# print("최초:",Student.kor) 

# s1 =Student(10)
# print(s1.no)
# Student.kor = 50 #클래스변수사용

# s2 =Student(20)
# print(s2.no)

# #---------------------------

# s1 = Student() ##객체선언
# s1.no = 1
# s1.name = "홍길동"
# print(s1) # 클래스값만으로는 주소값만 출력
# print(s1.name) #변수명까지 넣어야 출력

# s2 =Student(2)# 생성자 정의가 있어야 출력
# print(s2.no) #클래스 변수 >  클래스명.변수명, 클래스명.함수명


#1. 학생성적입력
#이름,국어,영어,수학 > 번호,이름,국어,영어,수학,합계,평균,등수
#클래스 1개가 생성이 되고
#클래스에 참조변수를(__str__) 입력해서  출력 해보세요




# print("학생성적입력")
# name = input("이름입력>>")
# kor = int(input("국어점수>>"))
# eng = int(input("영어점수>>"))
# math = int(input("수학점수>>"))
# s1 = Student(name,kor,eng,math)

# print("학생성적출력")
# print()
