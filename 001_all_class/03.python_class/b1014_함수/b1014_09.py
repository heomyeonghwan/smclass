#함수 - 매개변수(일반변수,복합변수)
# #1.!!!!! 함수 일반 매개변수 > return이 아니면 값이 함수밖으로 나올수없다
# def calc(h):
#   h +=100
#   return h
# h = 20
# #h = calc(h) #호출만 하고 일반변수 값을 넣어주지 않으면 값이 변경되지않음.
# calc(h) #호출만 하면값이 변경되지않음
# print(h)

# #2. 전역변수 - 일반매개변수 return없이 함수 밖으로 값사용
# def calc():
#   global h
#   h += 100

# h=20
# calc() #함수 호출후 h에 값을 할당할 필요없음
# print(h)

# #3.!!!!! 함수 복합매개변수 - return 없이 함수밖 값 사용
# def calc(hArr):
#   for i in range(len(hArr)):
#     hArr[i] += 100

# hArr = [1,2,3,4,5] #복합변수 - 주소값이 저장됨
# calc(hArr)
# print(hArr)



def calc(a):
  a += 10
  print(a)
  
a=10 #전역변수
calc(a)