def operate(count):
  for i in range(count):
    print("한국어 인사 : 안녕하세요.")

while True:
  print("[외국어 인사]")
  print("1. 영어 인사")
  print("1. 일본어 인사")
  print("1. 중국어 인사")
  print("1.프랑스어 인사")
  count = int(input("한국어 반복횟수를 선택하세요.(3)>>"))
  choice = input("원하는 항목번호를 선택하세요.(1)>>")
  
  if choice == "1":
    operate(count) ##함수호출
    print("영어 인사 : 헬로우, (Hello)")
  elif choice == "2":
    operate(count)
    print("일본어 인사 : 오하이요, (Ohayo)")
  elif choice == "3":
    operate(count)
    print("중국어 인사 : 니하오, (Ni Hau)")
  elif choice == "4":
    operate(count)
    print("프랑스어 인사 : 봉주르, (Bonjour)")