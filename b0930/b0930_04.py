# #name, kor, eng , math, total,avg 출력
#input으로 입력을받아
#홍길동,100,100,99 합계,평균(소수점2자리) 1줄에 출력
#format 사용, f 함수 사용
name = input("이름입력")
kor = input("국어점수")
#kor = int(input("국어점수"))
eng = input("영어점수")
math = input("수학점수")
total = int(kor)+int(eng)+int(math) #문자열에서 정수형으로 변경
avg = total/3

print("{},{},{},{},{},{:.2f}".format(name,kor,eng,math,total,avg))
print(f"{name},{kor},{eng},{math},{total},{avg:.2f}")









# a='100'
# b="200"
# print(type(a))
# print(type(b))

# print(a+b)#문자 연결연산자 100200
# print(int(a)+int(b)) #타입변경
# name= "홍길동"
# #print(int(name))# 문자를 숫자로 변경 불가능
# c="3.14"
# print(int(float(c)))#실수형으로 변경후 정수형으로 변경
# #print(int(c))#문자 실수형은 정수로 바로 변경불가
# print(str(c))#실수형을 문자열로 변경

# d= "True"
# print(bool(d)) #문자 불형을 불형으로 변경
# #타입변경 - str,float,int,bool




# #변수 bool논리형 int정수 float실수 str문자열

# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True #True,False 대문자로 넣어야함
# print(type(a_bool))





# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3
# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)