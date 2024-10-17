####예외처리 : try - except 구문 사용해서 처리
###예외가 발생되는  시점에 사용 에러없이 프로그램실행(에러일어나면 except로 옮기고 빠져나옴)

# print("프로그램 시작")
# # try: #
# #   # print("프로그램시작) ##구문오류 - 프로그램이 실행전에 오류
# #   print(list_a) ##런타임 오류 - 프로그램 실행중에 오류

# # except: # 처리할수있는 문구
# #   print("에러가 발생")

# print("프로그램 종료")



##

# #원의 넓이 원 둘레 구하기
# num = int(input("반지름을 입력하세요.>>"))
# print("원넓이:",(num**2)*3.14)
# print("원둘레 : ",2*num*3.14)


# n_str = input("반지름을 입력하세요.>>")
# if n_str.isdigit():
#   num = int(n_str)
#   print("원넓이:",(num**2)*3.14)
#   print("원둘레 : ",2*num*3.14)

# else:
#   print("정수가 아닙니다")


# n_str = input("반지름을 입력하세요.>>")
# try:
#   num = int(n_str)
#   print("원넓이:",(num**2)*3.14)
#   print("원둘레 : ",2*num*3.14)

# except Exception as e:
#   print("정수가 아닙니다",e)



## try - except
# list_a = [1,2,3,4,5,"홍길동"]
# list_b = []
# #숫자에 제곱을 하는 프로그램을 구현
# for a in list_a:
#   list_b.append(a**2)

# print(list_b)


# list_a = [1,2,3,4,5,"홍길동",5,6,7]
# list_b = []
# #숫자에 제곱을 하는 프로그램을 구현
# try:
#   for a in list_a:
#     list_b.append(a**2)
# except Exception as e:
#   print(e)
# print(list_b)

# ###  try - except 구동원리!!!!
#ㅅtry에 에러가 발생하면 except 실행
# print("1")
# try: #try 구문에 에러가 발생해야 except 실행시킴
#   print("2")
#   #print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")

# print("7")
# print("8")


#try - except - else
#else는 try구문에 에러가 없으면 실행/ 트라이 구문에 넣는거랑 같아서 안씀

# print("1")
# try: #try 구문에 에러가 발생해야 except 실행시킴
#   print("2")
#   #print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# else:
#   print("프로그램 에러가 발생하지않으면 실행됨")
# print("7")
# print("8")

#try - except - finally
#try가 에러나도 안나도 finally무조건실행
# print("1")
# try: #try 구문에 에러가 발생해야 except 실행시킴
#   print("2")
#   print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# else:
#   print("프로그램 에러가 발생하지않으면 실행됨")
# finally:
#   print("finally 실행됨")
# print("7")
# print("8")


# ##finally 쓰는 예시
# print("파일 open")
# try:
#   print("글1")
#   print("글2")
#   print("글3")
#   print("str > 딕셔너리입력4") #에러
#   print("글5")
#   print("글6")
#   print("파일 close")
# except:
#   print("잘못된 타입이 들어왔습니다")
#   print("파일 close")
# finally:
#   print("파일 close") # try,except에 파일 close를 안해도됨
# print("프로그램을 종료")

# f = open("b1017/a.txt","w",encoding="utf-8")
# try:
#   f.write("안녕하세요1\n")
#   f.write("안녕하세요2")
#   f.write("안녕하세요3")
#   f.write({"a":1})
#   f.write("안녕하세요4")
# except Exception as e:
#   print(e)
# finally:
#   f.close()

numbers = [52,273,32,103,90,10,275,1,2,1,2,12]
# a = "12351200"
# b = a.find("1")
# print(b)
try:
  print(numbers.index(52))
  print(numbers.index(1))
  print(numbers.index(3))# 없는거 에러(index)
  print(numbers.index(32))
  print(numbers.index(90))
except Exception as e:
  print("찾는 번호가 없습니다.",e)