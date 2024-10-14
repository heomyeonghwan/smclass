
# def num_sum(st,end):  ##(매개변수,매개변수)
#   sum = 0 ##지역변수
#   for i in range(st,end):
#     sum += i
#   print("합계 : ",sum)

# # #1~10까지 합계를 출력하시오
# # num_sum(1,11)

# # #1~100
# # num_sum(1,101)

# # #2~50
# # num_sum(2,51)

# # #100~1000
# # num_sum(100,1001)

# #두수를 입력받아 그사이 숫자 합을 구하시오
# #num1,num2 함수를 사용해서 출력하시오
# #1
# # num1 = int(input("숫자를 입력>>"))
# # num2 = int(input("숫자를 입력>>"))
# # num_sum(num1,num2)

# #2
# num_sum(int(input("숫자를 입력>>")),int(input("숫자를 입력>>")))




# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end):
#     sum += i
#   return sum

# # num1 = int(input("숫자를 입력>>"))
# # num2 = int(input("숫자를 입력>>"))
# # print(num_sum(num1,num2))

# # print("프로그램종료")


# # #1~10합과 1~100까지 합의 총합
# # total = 0
# # num_sum(1,11)
# # num_sum(1,101)
# # total = num_sum(1,11)+num_sum(1,101)

# # print("합계 : ",total)
# # print("프로그램종료")

# ##2~50 합 3~7합 5~50까지 합을 모두 더해서 출력
# total = 0
# print(f"2~50까지의 합 : {num_sum(2,51):,d}") ##.2f
# print("3~7까지의 합 : ",num_sum(3,8))
# print("5~50까지의 합 : ",num_sum(5,51))
# total = num_sum(2,51)+num_sum(3,8)+num_sum(5,51)
# print("합계 : ",total)


# def plus(n1,n2):
#   result = n1+n2
#   return result

# # def plus(n1,n2): ##위와 같음
# #   return n1+n2

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))

#두수를 입력받아 더하기를 출력하시오
def plus(n1,n2):
  result = n1+n2
  return result

n1= int(input("숫자입력"))
n2= int(input("숫자입력"))
print(plus(n1,n2))