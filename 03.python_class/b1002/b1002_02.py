# a = 100
# #if문 :을 넣음 if문 안쪽은 들여쓰기 해줘야 함.
# if a>10:    ##(a>10) 괄호 써도됨  ##if 문에는 1줄이 있어야 에러가 나지않음
#   print("10보다 큼")

# if a>10:    
#   ##if 문에는 1줄이 있어야 에러가 나지않음
#   pass


#숫자를 입력받아 100보다 큰수인지 작은수인지 100인지 출력하시오.
num = (int(input("숫자입력")))
if num>100:
  print("100보다큼")
elif num==100:
  print("100임")
else:
  print("100보다 작음")