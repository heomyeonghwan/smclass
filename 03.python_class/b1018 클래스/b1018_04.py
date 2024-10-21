#절차적인 형태의 프로그램 구현
#반지름을 입력받아 원의 둘레와 넓이를 출력
# 넓이: 3.14*반지름*반지름
#둘레: 3.14*2*반지름

# r = int(input("반지름을 입력"))
# print(f"원 넓이:{3.14*r*r:.2f}")
# print("원 둘레:",3.14*2*r)


#클래스 생성
class Circle:
  def __init__(self,length):
    self.__length = length #변수에 직접적으로 접근제한 : __

  def get_area(self):
    return 3.14*self.__length**2
  def get_circum(self):
    return 3.14*2*self.__length

#클래스 선언
c1 = Circle(int(input("반지름을 입력")))
c1.length = 7
print("넓이 : ",c1.get_area())
print("둘레 : ",c1.get_circum())

c2 = Circle(int(input("반지름을 입력")))
print("넓이 : ",c2.get_area())
print("둘레 : ",c2.get_circum())