import random

r_num = random.randint(1,100)
list=[]
count=0
for i in range(10):
    num = int(input(f"{i+1}번째 숫자를 입력해주세요>>"))
    list.append(num)
    print(list)
    if num > r_num:
        print(f"{num}보다 작은 숫자입니다.")
        print(f"{9-i}회 남았습니다. 다시입력해주세요")
    elif num < r_num:
        print(f"{num}보다 큰 숫자입니다.")
        print(f"{9-i}회 남았습니다. 다시입력해주세요")
    elif num == r_num:
        print(f"정답입니다. 정답: {r_num}")
        count=1
        break
if count==0:
    print("10회도전 실패! 정답:",r_num)