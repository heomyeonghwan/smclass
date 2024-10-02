import random
r_num = random.randint(0,100)
#while
i=0
count=0

while i<10:
  print(f"{i+1}번째 도전")
  num = int(input("숫자입력"))
  if num >r_num:
    print("입력한숫자가 큼")
  elif num <r_num:
    print("입력한숫자가 작음")
  elif num ==r_num:
    print("정답. 정답번호:",r_num)
    count=1
    break
  i+=1
if count ==0:
  print("10번도전에 실패! 정답번호:",r_num)
  