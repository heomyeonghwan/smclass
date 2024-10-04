##range - (시작값,끝값+1,증가값<1일때 생략>)
# for i in range(1,10,1):
# for i in range(1,10,2):


# #1~10 까지 for 문을 사용하여 출력
# for i in range(1,10+1):  #11로 해도 무관
#   print(i)

# #1,3,5,7,9 까지 출력
# for i in range(1,10):
#   if i%2!=0:
#     print(i)

# # 구구단 출력
# for i in range(2,9+1):
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#     print(f"{i}x{j}={i*j}")
#   print("-"*20)

# # 구구단 1,3,5,7,9 단 출력
# for i in range(1,9+1):
#   if i%2!=0:
#     print(f"[{i}단]")
#     for j in range(1,9+1):
#       print(f"{i}x{j}={i*j}")
#     print("-"*20)


#for문을 사용해서
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#   print("*"*i) # 1,2,3,4,5

# for i in range(5,0,-1): #역순
#   print("*"*i)

# for i in [1,2,3]:
#   #print("안녕하세요")

#배열이 1 - 1번출력, 2 - 2번출력 3 - 3번출력
# #1번째 방법
# for i in [1,2,3]:
#   print("안녕하세요.\n"*i,end="")
#   print("-"*30)
# #2번째 방법
# for i in [1,2,3]:
#   for j in range(i):
#    print("안녕하세요")
#   print("-"*30)


# # 0:안녕하세요.
# # 1:안녕하세요.
# # 2:안녕하세요.
# for i in range(3):
#   print(f"{i}:안녕하세요.")
# for _ in range(3): ##변수 x
#   print("안녕하세요.")


#1~100까지 숫자의 합을 구하시오
# sum = 0
# for i in range(1,100+1):
#   sum += i
# print("합계:",sum)

# #1,3,5,7,9...99합계
# sum = 0
# for i in range(1,100+1,2):
#   sum+=i
# print("합계:",sum)

# for i in range(1,100+1):
#   if i%2 !=0:
#     sum+=i
# print("합계:",sum)

# #1. 두수를 입력받아 두수 포함 전체 합계 구하기
# num1 = int(input("숫자입력"))
# num2 = int(input("숫자입력"))
# min = num1; max = num2
# if num1>num2:
#    min=num2;max=num1
   
# sum = 0
# for i in range(min,max+1):
#    sum+=i
# print("합계:",sum)

# #2. 두수를 입력받아 두수 포함 전체 합계 구하기(min,max 함수활용)
# num1 = int(input("숫자입력"))
# num2 = int(input("숫자입력"))
# min = min(num1,num2);max=max(num1,num2)
# sum = 0
# for i in range(min,max+1):
#    sum+=i
# print("합계:",sum)

# #3. 두수를 입력받아 두수 포함 전체 합계 구하기(min,max 함수활용2)
# num1 = int(input("숫자입력"))
# num2 = int(input("숫자입력"))

# sum = 0
# for i in range(min(num1,num2),max(num1,num2)+1):
#    sum+=i
# print("합계:",sum)



#4 if 사용 
num1 = int(input("숫자입력"))
num2 = int(input("숫자입력"))
if num1>num2:
  num1,num2=num2,num1 #파이썬만 가능 - 두개변수 취환
  # num3=num1  #다른언어는 변수를 하나더 만들어 야함
  # num1=num2
  # num2=num3

sum = 0
for i in range(num1,num2+1):
   sum+=i
print("합계:",sum)