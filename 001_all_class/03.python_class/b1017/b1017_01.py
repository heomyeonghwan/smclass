###
# subject = ["국어","영어"]

# #함수선언
# def output(subject):
#   #출력
#   print("[과목]")
#   print("-"*20)
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요.>>")
#   #list > append
#   subject.append(s_input)
#   #함수 호출
#   output(subject) 


###
a = 10 #전역변수(호출 위에만 있으면됨)

# #함수선언
# def func():
#   a=50 #지역변수 - 함수를 종료하면 모두 제거됨
#   print("함수 내 a:",a)

# #함수 호출(함수 선언 밑에 있어야함)
# func()
# print("함수 밖 a:",a)

# #함수선언
# def func():
#   global a  #전역변수를 가져옴
#   print("함수 내 a:",a)
#   a += 50

# #함수 호출(함수 선언 밑에 있어야함)
# func()
# print("함수 밖 a:",a)

# #함수선언
# def func(a):
#   print("함수 내 a:",a)
#   a += 50
#   return a

# #함수 호출(함수 선언 밑에 있어야함)
# a = func(a)
# print("함수 밖 a:",a)

# ###
# a = 10
# b = 20
# sum = 0

# #함수 선언
# def add(a,b):
#   return a+b
# #함수 호출
# sum = add(a,b)
# print("a+b :",sum)

# ###
# a = 10
# b = 20
# c = 30
# #a에 함수사용하여 a,b,c 합을 입력해서 a에 저장 및 출력

# # def add(a,b,c):
# #   a = a+b+c
# #   print(a)
# #   return a
  
# # a= add(a,b,c)
# # print(a)

# # #간단하게
# # def add(a,b,c):
# #   return a+b+c
  
# # a= add(a,b,c)
# # print(a)


###
subject = ["국어","영어","수학","과학","역사"]
score = []

while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("d원하는 번호를 입력>")
  if choice =="1":
    s_input = input("과목을 추가하세요>")
    subject.append(s_input)
  elif choice == "0":
    break

  
for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수 입력>>")))
sum=0
for i in range(len(subject)):
  print(f"{subject[i]}:",score[i])
  sum +=score[i]
print("합계:",sum)



