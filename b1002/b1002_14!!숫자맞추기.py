import random

#1~100 까지의 랜덤숫자를 생성
#입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
#입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
#10번 도전하기 정답을 맞추면 정답입니다. 프로그램 종료 break
#for문 while문 2가지

r_num = random.randint(1,100) ##조건식 안에 있으면 랜덤숫자가 할때마다 변경됨/while 밖에있어야함

# #while문
# count = 0
# i=0 #초기값
# while i<10: #조건식
#   num = int(input("숫자를 입력하시오")) ##
#    #비교구문
#   if num > r_num:
#     print("입력한숫자가 큽니다.")
#   elif num < r_num:
#     print("입력한 숫자가 작습니다.")
#   elif num == r_num:
#     print("정답입니다. 정답번호: ",r_num)
#     count = 1
#     break
#   i+=1 #증감식

# # 10번 도전에  실패할경우
# if count ==0:
#   print("10번도전에 실패하셨습니다. 정답번호: ",r_num)


#for문
count=0
for i in range(10):
  num = int(input("숫자를 입력하시오"))
  if num > r_num:
    print("입력한숫자가 큽니다.")
  elif num < r_num:
    print("입력한 숫자가 작습니다.")
  elif num == r_num:
    print("정답입니다. 정답번호: ",r_num)
    count = 1
    break
# 10번 도전에  실패할경우
if count ==0:
  print("10번도전에 실패하셨습니다. 정답번호: ",r_num)

  


