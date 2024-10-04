import random

#랜덤 숫자 생성 - random
####random() : 0<=x<1 실수값 추출
print(random.random())
#0-9
print(int(random.random()*10))
#1-10
print(int(random.random()*10)+1)

# 랜덤 int 추출 - 1~10까지, 10포함 - randint
print(random.randint(1,10)) 

#랜덤 범위 추출 - 1,10사이 (10포함X) - randrange
print(random.randrange(1,10))

#list에서 랜덤 추출
a=[1,4,5,9]
print(random.choice(a))

#list에서 여러개 랜덤 추출(중복가눙) - choices
print(random.choices(a,k=2))

#list에서 여러개 랜덤 추출(중복불가) - sample
print(random.sample(a,2))