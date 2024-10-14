
#함수사용
# def calc(num,num2):
#   print(f"두수 더하기 :{num+num2}")
#   print(f"두수 빼기 :{num-num2}")
#   print(f"두수 곱하기 :{num*num2}")
#   print(f"두수 나누기 :{num/num2}")

# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num)):
#   calc(num[i],num2[i])



# #for 문을 활용한 계산
# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num)):
#   print(f"두수 더하기 :{num[i]+num2[i]}")
#   print(f"두수 빼기 :{num[i]-num2[i]}")
#   print(f"두수 곱하기 :{num[i]*num2[i]}")
#   print(f"두수 나누기 :{num[i]/num2[i]}")



#
# def calc(num,num2):
#   print(f"두수 더하기 :{num+num2}")
#   print(f"두수 빼기 :{num-num2}")
#   print(f"두수 곱하기 :{num*num2}")
#   print(f"두수 나누기 :{num/num2}")
 

# num = int(input("숫자를 입력>>"))
# num2 = int(input("숫자를 입력>>"))

# calc(num,num2)

# ##문자열을 숫자로 변경
# def calc(num,num2):
#   print(f"두수 더하기 :{num+num2}")
#   print(f"두수 빼기 :{num-num2}")
#   print(f"두수 곱하기 :{num*num2}")
#   print(f"두수 나누기 :{num/num2}")
 

# numStr = input("숫자를 입력>>(12,5)")
# numStr2 = numStr.split(",")

# num = int(numStr2[0])
# num2 = int(numStr2[1])
# calc(num,num2)

### 3가지 수를 입력받아
# def calc(num,num2,num3):
#   print(f"세수 더하기 :{num+num2+num3}")
#   print(f"세수 빼기 :{num-num2-num3}")
#   print(f"세수 곱하기 :{num*num2*num3}")
#   print(f"세수 나누기 :{num/num2/num3}")

# numStr = input("숫자를 입력>>(12,5,3)")
# numStr2 = numStr.split(",")

# num = int(numStr2[0])
# num2 = int(numStr2[1])
# num3 = int(numStr2[2])

# calc(num,num2,num3)

# #배열
# def calc(numStr2): 
#   s1=0
#   s2=0
#   s3=1
#   s4=1
#   for i in range(len(numStr2)):
#     s1 += numStr2[i]
#     s2 -= numStr2[i]
#     s3 *= numStr2[i]
#     s4 /= numStr2[i]
#   print(f"두수 더하기 : {s1}")
#   print(f"두수 빼기기 : {s2}")
#   print(f"두수 곱하기 : {s3}")
#   print(f"두수 나누기 : {s4}")


# numStr = input("숫자를 입력>>(12,5,3)")
# numStr2 = numStr.split(",")
# numStr2 = [int(i) for i in numStr2] ##리스트 내포
# print(numStr2)

# calc(numStr2)


# #기본 매개변수- 매개변수의 개수가 동일
# def calc(n1,n2): 
#   print(n1+n2)
  
# calc(1,2)

#가변 매개변수
# def calc(*n): 
#   print(n)
#   print(len(n))

# calc(1,2,3,4,5,6,7)



# ##키워드 매개변수
# def calc(n1 = 10,n2=20): 
#   print(n1)
#   print(n2)

# calc()
# calc(30) #n1 > 30, 20 #키가 없으면 1번째자리로
# calc(n2=100) #n2 > 10, 100 #키가 있으면 키값자리로

# print(1,2,3,sep=":",end="\t") #가변매개변수
# print("안녕")


# #함수 내에  선언된 변수는 외부에서 사용할 수 없다.(return으로 받아야함)
# def calc(v1,v2):
#   sum = 0            #지역변수
#   for i in range(v1,v2+1):
#     sum += i
#   return sum


# sum = calc(1,10)
# print(sum)



# def calc(v1,v2):
#   global sum     #전역변수(외부의 있는 변수 값을 가지고와서 쓸수있다)
            
#   for i in range(v1,v2+1):
#     sum += i
#   return sum   #return 으로 외부로 내보냄(해도되고 안해도됨)

# sum= 100   #외부의 변수를 사용해서 계산을 하고싶을경우
# sum = calc(1,10)
# print(sum)

#return을 뺼경우
def calc(v1,v2):
  global sum     #전역변수(외부의 있는 변수 값을 가지고와서 쓸수있다)
            
  for i in range(v1,v2+1):
    sum += i
   
sum= 100   #외부의 변수를 사용해서 계산을 하고싶을경우
calc(1,10)
print(sum)


# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2
#   s4 = n1/n2
#   s5 = [s1,s2,s3,s4]
#   #return s1,s2,s3  ##파이썬만 여러값 가능
#   return s5

# s5 = calc(10,5)
# # print(s1)
# # print(s2)
# # print(s3)
# print(s5)

# print("프로그램 종료")


##매개변수가 일반변수일 경우 return하지않으면 변수값이 변동 없음
# hh=100

# def add(hh):
#   hh = hh +100
#   return hh

# add(hh)
# print(hh)


#-------------------------------------------------
#복합변수 - 매개변수로 전달이 되면 ,return 없어도 값이 변경되어 전달 됨(리스트 딕셔너리)
hong = [1,2,3,4,5]

def add(h):
  for i in range(len(h)):
    h[i] = h[i]+100
add(hong)
print(hong)

# kim = []

# kim = hong   ##얕은 복사
# kim[0] = 100
# print(hong)


#전역변수 경우 함수내에서도 사용가능하고 외부에서도 사용가능함
#지역변수는 return 없이는 값이 함수밖으로 나오지못함
def calc():
  global sum  #전역변수 인경우 ,  함수에서 변경시 외부에서도 같이 변경이됨
  sum =100
sum=10
calc()#함수에서 sum을 200으로 변경이됨
print(sum) #결과값은 sum 200이됨