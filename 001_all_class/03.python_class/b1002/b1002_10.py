fruit = []
# a=0
# while a<10:
#   a += 1
#   print(a)

# print("프로그램 종료")

# while True:  ##True 무한대로 실행(무한반복):while True
#   print(a)
#   a += 1


# 반복문 종료할떄 : break
# while True:
#   break
# print("프로그램 종료")

while True:
  ##strip() 앞쪽여백, 뒤쪽여백 제거 : ' 사과' > '사과'
  ##replace(" ",""):문자대체함수(안쪽여백까지 제거)
  search = input("과일이름을 입력.(종료:x)").replace(" ","")
  #search = input("과일이름을 입력.(종료:x)").strip()
  if(search == 'x'):
    break

  #입력된 과일이름을 리스트에 추가하시오
  if search in fruit:
    print("같은 이름이있습니다.")
  else:
    print(f"{search}을(를) 추가합니다,")
    fruit.append(search)
    print("모든 과일: ",fruit)
 
