#
def plus(a): #기본매개변수의 값전달은 무조건 리턴해서 돌려줘야함//값전달,리턴필요
  a += 50
  print("지역변수 a:",a) #
  return a
a = 10
a = plus(a)
print("전역변수 a:",a) #

def plus(a): # 복합매개변수(리스트,딕셔너리)의 값전달은 리턴 돌려줄필요없음//값전달만 필요
  a[0] = 100
  a[1] = 200
  print("지역변수 a:",a) #[100,200]
  
a = [10,20] 
plus(a)
print("전역변수 a:",a) #