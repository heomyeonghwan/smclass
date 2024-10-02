students =[
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
]

ss = [4,'강감찬',100,90,99]

# print(students) ##1개씩 가져와서 출력

# for s in students:
#   print(s) ##한번에 모두출력

# #이름이 유관순인것을 출력
# for s in students:
#   if s[1] == '유관순':
#     print(s)

# students에 ss를 추가
students.append(ss)
print(students)

#값이 2개 이상 저장하려면, 주소값
#이순신인 데이터를 삭제 remonve
# for s in students: ## [1,'홍길동',100,90,99],[2,'유관순',100,100,99],[3,'이순신',100,100,99],[4,'강감찬',100,90,99]
#   if s[1] == '이순신':
#     students.remove(s)
    
for idx,s in enumerate(students): ##del 삭제
  if s[1] == '이순신':
    del students[idx]
    


print(students)