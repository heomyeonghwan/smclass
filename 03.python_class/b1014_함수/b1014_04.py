# 함수선언
def calc(n1,n2,op):
  if op =="+":
    return n1+n2
  elif op =="-":
    return n1-n2
  elif op =="*":
    return n1*n2
  elif op =="/":
    return n1/n2
while True:
  n1= int(input("숫자입력"))
  n2= int(input("숫자입력"))
  op = input("+,-,*,/ 하나를 선택하세요")

  print("결과값 : ",calc(n1,n2,op))


