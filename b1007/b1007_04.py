import random

###1~25까지 사이의 랜덤숫자를 생성해서 출력하시오.
# #num = int(random.random()*25)+1

# num = random.randint(1,25)
#25번 반복해서, 1~25까지 랜덤숫자를 입력, 중복은 제거하고 출력하시오
# a_list = []

# for i in range(25):
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)
# print(a_list)


# #1~25 랜덤으로 배치
# a_list = []
# while len(a_list)<25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)
# print(a_list)
# print(len(a_list))

#1~25 랜덤으로 배치2 random.sample()
a_list = []
for i in range(25):
  a_list.append(i+1)
# b_list = random.sample(a_list,25) #범위 리스트, 25개추출(중복추출 안됨)
# print(b_list)
# b_list = random.choices(a_list,k=25) ##범위 리스트, 25개추출(중복추출 rksmd)
# print(b_list)