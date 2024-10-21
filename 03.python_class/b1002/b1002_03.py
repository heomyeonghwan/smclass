# #입력한 숫자가 짝수인지 홀수인지 출력
# num = int(input("숫자입력"))
# if num%2==0:
#   print("짝수")
# elif num==0:
#   print("0")
# else:
#   print("홀수")

# #입력한 숫자가 1(포함)보다 크고 10(포함)보다 작을때만 정답, 그렇지않으면 오답
# num = int(input("숫자입력"))
# if 1<=num<=10: #>>1<=num<=10 파이썬만 가능 ,  #if num>=1 and num<=10
#   print("정답")
# else:
#   print("오답")

# #입력한 숫자가 10(포함)보다 작거나 100(포함)보다 클때 정답,아니면 오답
# num = int(input("숫자입력"))
# if num<=10 or num>=100:
#   print("정답")
# else:
#   print("오답")

# #3,4,5월 봄 6,7,8여름 9,10,11가을 12,1,2겨울 입니다.그외는 잘못된 숫자
# num = int(input("숫자입력"))
# if 3<=num<=5:
#   print("봄")
# elif 6<=num<=8:
#   print("여름")
# elif 9<=num<=11:
#   print("가을")
# elif num==12 or 1<=num<=2:
#   print("겨울")
# else:
#   print("다시입력")

#100,99,98 a+ 97,96,95,94, a 93,92,91,90 a- 89,88 b+ 87~84 b .c:70점대.d:60점대. f:60점이하
score = int(input("점수입력"))
# if 98<=score: #뒤에 생략가능
#   print("A+")
# elif 94<=score:
#   print("A")
# elif 90<=score:
#   print("A-")
# elif 88<=score:
#   print("b+")
# elif 84<=score:
#   print("b")
# elif 80<=score:
#   print("b-")
# elif 78<=score:
#   print("c+")
# elif 74<=score:
#   print("c")
# elif 70<=score:
#   print("c-")
# elif 68<=score:
#   print("d+")
# elif 64<=score:
#   print("d")
# elif 60<=score:
#   print("d-")
# else:
#   print("f")

# ###중첩 이프문
# scores ="";
# if 90<= score:
#   scores ="a"
#   if 98<= score:
#     scores+="+"
#   elif 90<= score<=93:
#     scores+="-"
# elif 80<=score:
