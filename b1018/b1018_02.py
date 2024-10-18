# class 생성 방법


#학생 1명정보
# 번호,이름,국어,영어,수학,합계, 평균,등수
#학생 클래스 설계도 생성
class Student:    # 클래스 구조
  #생성자     
  # def __init__(self):  # 기본생성자
  #   None            

  def __init__(self,no,name,kor,eng,math):   ##매개변수가 있는 생성자
    self.no = no
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
  
  def print():
    print("{self.no}\t{self.name}\t{self.kor}\t{self.eng}\
          \t{self.math}\t{self.total}\t{self.avg}\t{self.rank}\t")
#클래스 사용방법
#클래스 선언
s1 = Student(1,"홍길동",100,100,100)
s1.print()
#print(s1.no,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,s1.rank)
#print(s1) #값이 아닌 주소값 출력됨

#클래스명.변수명 = 값 : 변수가 생성되어 클래스에 변수가 저장됨
##기본생성자를 사용해서 값을 개별적으로 입력방식
# s1 = Student
# s1.no = 1
# s1.name = "홍길동"
# s1.kor = 100
# s1.eng = 100
# s1.math = 100
#클래스내 변수출력
# print(s1.no)
# print(s1.name)

# s2 =  Student()
# s1.no = 2
# s1.name = "유관순"
# s1.kor = 100
# s1.eng = 100
# s1.math = 100



#전체학생리스트 정보
class Students:
  pass