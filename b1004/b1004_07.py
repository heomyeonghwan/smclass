# i=0
# while i<10:
#   print(i)
#   i+=1

# for i in range(10):
#   print(i)

# #구구단을 출력
# i=1
# while i<10:
#   j=1
#   while j<10:
#     print(f"{i}x{j}={i*j}")
#     j+=1
#   i+=1

# for i in range(1,10):
#   for j in range((1,10)):
#     print(f"{i}x{j}={i*j}")


# i=0
# while True:  ##무한반복
#   print(i); i+=1


# #입력한 숫자를 계속 더하는 프로그램을 만드시오
# # 0 이 입력되면 프로그램 종료
# #반복문 종료는 : break

# sum=0
# while True:
#   num=int(input("숫자를입력"))
#   if num == 0:
#     print("프로그램 종료")
#     break
#   sum+=num
#   print("합계:",sum)

# i=0;j=0
# while i<10:
#   print("번호1:",i)
#   while j<10:
#     if j==5:
#       break #j 반복문만 종료
#     print("번호2:",j)
#     j+=1

# #이중 while 문 i=1,10 ,j=1,10 - j의 출력을 1,3,567,9

# i,j=1,1
# print(i,j)


# i,j = 1,1
# while i<10:

#   while j<10:
#     if j%2==0:
#       j+=1
#       continue
#     print(i,j)
#     j+=1
#   j=1;i+=1


# #두수를 입력받아,+,-,*,/

# while True:
#   num = int(input("숫자를 입력"))
#   num2 = int(input("숫자를 입력(종료:0)"))

#   if num2 ==0:
#     break
#   print("[두수의 사칙연산]")
#   print("-"*50)
#   print("1. 두수 더하기")
#   print("2. 두수 빼기")
#   print("3. 두수 곱하기")
#   print("4. 두수 나누기")
#   print("-"*50)
#   choice = int(input("원하는 번호를 입력"))
#   if choice == 1:
#     print("결과값 :",num+num2)
#   elif choice == 2:
#     print("결과값 :",num-num2)
#   elif choice == 3:
#     print("결과값 :",num*num2)
#   elif choice == 4:
#     print("결과값 :",num/num2)


s_list = []
no = 1
while True:
  #이름,국어,영어,수학 입력을 받아 번호,이름,국어,영어,수학,합계,평균 출력
  name = input("이름을 입력하세여.(종료:0)")
  if name == '0':
    break
  kor = int(input("국어점수 입력하세여"))
  eng = int(input("영어점수 입력하세여"))
  math = int(input("수학점수 입력하세여"))
  print(f"번호:{no}, 이름:{name}, 국어:{kor}, 영어:{eng}, 수학:{math},\
         합계:{kor+eng+math}, 평균:{(kor+eng+math)/3:.2f},")
  no+=1
print("프로그램을 종료합니다.")