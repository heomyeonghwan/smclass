# aArr = [2,3,4,6,7,8,9,10]
# #50,100 추가
# aArr.append(50)
# aArr.append(100)
# print(aArr)

# #2번자리에 30 추가
# aArr.insert(2,30)
# print(aArr)

# #숫자 6 삭제
# aArr.remove(6)
# print(aArr)

# #index0,3 데이터를 삭제
# del aArr[0]
# del aArr[3]
# print(aArr)

# a=[1,'홍길동',100]
# b=[1,'홍길동',200]
# c=[1,'홍길동',100]

# if a==b:
#   print("같음")
# else:
#   print("다름")

# if a==c:
#   print("같음")
# else:
#   print("다름")

# all_list = [
#   [1,'홍길동',100],[1,'유관순',200],[3,'이순신',100]
# ]
# a=[3,'이순신',100]

# # #데이터 값으로 삭제 -remove
# # all_list.remove(a)
# # print(all_list)

# #이름이 유관순인것을 삭제

# for s in all_list:
#   if s[1] == '유관순':
#    all_list.remove(s)
# print(all_list)


students =[
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]


# 이름을 입력받아 같은 이름이 있으면 데이터 삭제, 없으면 없음 출력
name = input("이름")
count = 0
for idx,s in enumerate(students):
  if s[1] == name:
   del students(idx)
   print(f"{name}을(를) 삭제합니다")
   count = 1
   break
  # else:
  #   print("없음")
if count == 0:
  print("찾고자하는 이름이 없습니다.")
print("현재학생의 성적:",students)