#1.
# while True:
#   score = 100
#   print("[나눗셈 프로그램]")
#   nstr = input("숫자만 입력가능>>")
  
#   if nstr.isdigit(): ##숫자로 변환가능한지
#     print("숫자로 변환가능")
#     num = int(nstr)
#     print("입력된숫자로 100을나눔:",score/num)
#   else:
#     print("숫자로 변환 안됨")


#2. try-except : 프로그램 예외를 처리하는 명령어
# while True:
#   score = 100
#   print("[나눗셈 프로그램]")
#   nstr = input("숫자만 입력가능>>")
#   #숫자가 아닌것을 입력하면 에러, 0을 입력하면 에러
#   try:
#     num = int(nstr)
#     print("입력된숫자로 100을나눔:",score/num)
#   except:
#     print("숫자로 변환 안됨")

try:
  print ("입력된숫자:",int(input("숫자를 입력하세요>> ")))
except:
  pass