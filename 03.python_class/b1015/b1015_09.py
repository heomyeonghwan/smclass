# def func(v):
#   return v*2

# print(func(2))
# #lambda v:v*2  -위에랑같음

#기본적인 함수사용

# aArr =[1,2,3,4]
# print(aArr)
# bArr=[]
# for a in aArr:
#   bArr.append(func(a))

# print(bArr)



# #리스트내포
# aArr =[1,2,3,4]
# print(aArr)
# bArr = [a*2 for a in aArr]
# print(bArr)


# #map 함수 - map(함수,리스트): 리스트의 내용을 1개씩 함수에 전달해서 결과값을 리스트로 저장
# aArr =[1,2,3,4]
# bArr = map(func,aArr)## map(함수,리스트)
# #bArr = list(map(func,aArr))## map(함수,리스트)
# print(type(bArr))
# print(list(bArr))


# bArr = list(map(lambda x:x*2,aArr))



# filter(함수, 반복가능한자료형) - 리스트,튜플,딕셔너리

# #기본 함수사용방법
# def func(v):
#   if v%2 ==0:
#     return v

# aArr = [1,2,3,4]
# bArr = []
# for i in aArr:
#   if func(i) != None:
#     bArr.append(func(i))
# print(bArr)

# #filter - 조건식에 맞는거만 뽑아냄
# def func(v):
#   if v%2 == 0:
#     return True
#   else:
#     return False
# # #aArr 값중에 2의배수인경우만 리턴
# # aArr = [1,2,3,4] 
# # bArr = list(filter(func,aArr))
# # print(bArr)

# #람다식 변경 - 함수들을 축약함 x > 매개변수, :x > 수식
# aArr = [1,2,3,4]
# bArr = list(filter(lambda x:x%2==0,aArr))
# print(bArr)


# #zip함수 : 2개리스트를 1개로 변경(묶음)
# a = [1,2,3,4]
# b = [10,20,30,40]
# print(list(zip(a,b))) #리스트 타입(안에 튜플로 들어감)
# print(dict(zip(a,b))) #딕셔너리 타입

# # 람다식 매개변수 2개
# def func(v1,v2):
#   return v1*v2

# lambda v1,v2:v1*v2


# ##
# a = [1,2,3,4]
# b = [10,20,30,40]
# aArr=[]
# # --- a+b = [11,22,33,44] 만들기----

# #리스트내포
# aArr = [i+j for i,j in zip(a,b)]
# print(aArr)

# #기본함수 사용
# def func(a,b):
#   for i,j in zip(a,b):
#     aArr.append(i+j)
#   return aArr
# print(func(a,b))

# def func(a): #리스트 하나보낼때
#   for i in a:
#     aArr.append(i*i)
#   return aArr
# print(func(a))

    
# #람다식 구현
# # map(lanbda 매개변수1,매개변수2:리턴값,복합자료형1,복합자료형2)
# aArr = list(map(lambda i,j:i+j,a,b))
# print(aArr)



#####퀴즈
a = [1,2,3,4,5]
#a 리스트에 전부 10을 더해서 리스트에 담아 출력하시오
#리스트 내포, map 람다식 사용

#리스트 내포
aArr=[i+10 for i in a]
print(aArr)

#람다식
#map() - 리스트에 모두다 동일한 형태를 적용시킬때
aArr= list(map(lambda x:x+10,a))
print(aArr)

###
#4*3*2*1

result = 1
for i in range(1,5):
  result *= i
print(result)

result = 1
for i in range(4,0,-1):
  result *= i
print(result)