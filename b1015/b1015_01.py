# #함수 - 기본매개변수,가변매개변수,키워드 매개변수

# #함수 선언
# def calc(st,end):
#   for i in range(st,end+1):
#     print(f"[{i}단]")
#     for j in range(1,10):
#       print(f"{i}X{j}={i*j}")
#   print("-"*60)

# #2~9
# #구구단
# calc(2,9) #함수호출

# #3~7
# calc(3,7) #함수호출

# #5~8
# calc(5,8) #함수호출



# #1.함수 - 기본매개변수
# def plus(n1,n2):
#   sum = n1 + n2
#   print("합계: ",sum)
# #함수호출 - 매개변수 개수를 정확히 맞춰야함, 맞추지않으면 애러발생
# plus(10,20)


# #2. 함수 - 가변매개변수
# def plus(a,*n1): #기본매개변수를 같이사용하려면, 가변매개변수 앞에 사용
#   print("a: ",a)
#   for i in n1:
#     print(i)
#   print(type(n1))#튜플: 수정불가 리스트

# plus(1,2,3,4,5)


#3. 함수 - 키워드 매개변수
def plus(k=10,m=5):
  print("k: ",k)
  print("m: ",m)
  print("-"*20)

plus()  #매개변수 개수가 일치하지않으면 애러지만 키워드 매개변수는 상관없음
plus(1)  #키값이 없으면 첫번째 자리로감
plus(m=1,k=2)  #순서가 바뀌어도 상관없음

#
print(1,2,3,sep=":",end="\t")
print(1)

#4.함수 - 가변매개변수,키워드 매개변수 동시 사용할 경우
def plus(*n,k=10): ##가변매개변수 먼저, 다음 키워드 매개변수 사용
  print("k : ",k)
  for i in n:
    print(i)

plus(1,2,3,4,5)
plus(1,2,3,4,5,k=50)