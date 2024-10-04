import random


#10 번 도전 입력숫자가 더크면 작은수를 입력해라
# 작으면 더큰수 입력해라
#10번 도전 실패시 

#랜덤숫자 : 1~100
r_num=random.randint(1,100)

i=0    #반복횟수 변수
count=0 #확인하는 변수
while i<10:
  print(f"{i+1}번째 도전!!!")
  num=int(input(f"{i+1}번째 숫자를 입력하세요."))
  if num>r_num:
    print("입력한 숫자가 더큽니다. 다시입력")
  elif num<r_num:
    print("입력한 숫자가 작습니다. 다시 입력")
  elif num==r_num:
    print("도전에 성공했습니다. 랜덤숫자:",r_num)
    count=1
    break
  i+=1

if count==0:
  print(f"10번도전에 실패! 랜덤숫자:{r_num}")