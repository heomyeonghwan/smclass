#문자열 슬라이싱

# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈"
# print(len(str)) ##총글자수

# #뒤쪽에서 5자리 전까지 출력
# print(str[-5:])
# print(str[-1])
# print(str[::-1])#거꾸로 다출력


# #list추가 - append 뒤에추가 insert 원하는 위치에 추가
# #삭제 del 위치삭제 remove 값으로 검색하여 삭제

# a_list=[1,2,3]
# #10추가
# a_list.append(10)
# print(a_list)
# a_list.insert(2,100)
# print(a_list)

# del a_list[1]  #index1번삭제
# print(a_list)
# a_list.remove(100)  #값으로 삭제
# print(a_list)


students =[
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
]
print(students)
print(students[0][3])
print(len(students))


# s = [4,'강감찬',100,90,99]
# #s 리스트에 합계,평균 추가
# s.append(s[2]+s[3]+s[4])
# s.append("{:.2f}".format((s[2]+s[3]+s[4])/3))
# print(s)

#합계 점수를 추가해서 출력

#반복문
for i in range(10): # 0부터 시작 10번반복
  print(i)

for i in range(2,5):  # 2부터 5 이전까지 반복
  print(i) 

for i in range(1,10,):  #index 1부터 10 이전까지 2씩 띄워서 반복
  print(i) 

aArr = [1,2,5,7,8]
for i in aArr:  #list의 값을 1개씩 가져와서 출력
  print(i)
# enumerate 는 index번호를 추가해서 가져올수있다
for i,data in enumerate(aArr):  #list의 값과 index번호를 함께출력
  print(i,":",data)

aStr = "안녕하세요"
for i in aStr:   #문자열의 값을 1개씩 가져와서 출력
  print(i)

for idx,data in enumerate(aStr):
  print(idx,":",data)  