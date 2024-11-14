students =[
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]
#   #찾는 학생이 있으면 찾는 학생이름이 있습니다, 없으면 찾는 학생이름이 없습니다.
#   #합계 평균추가
# search = input("찾을 학생 이름 입력")
# cnt=0
# for s in students:
#   if s[1] == search:
#     print("찾고자하는 학생이름이 있습니다.")
#     cnt=1
#     break
# if cnt==0:
#   print("학생의 이름이 없습니다.")

# for s in students:
#   s.append(s[2]+s[3]+s[4])
#   s.append("{:.2f}".format((s[2]+s[3]+s[4])/3))
# print(students)



# search = input("찾을학생이름")
# cnt=0
# for s in students:
#   if s[1]==search:
#     print("학생존재")
#     cnt=1
#     break

# if cnt==0:
#   print("찾는학생이 존재하지 않음")

# for s in students:
#   s.append(s[2]+s[3]+s[4])
#   s.append((s[2]+s[3]+s[4])/3)
# print(students)

#1~100 까지의 랜덤숫자를 생성
#입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
#입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
#10번 도전하기 정답을 맞추면 정답입니다. 프로그램 종료 break
# 10번 도전에  실패할경우
#for문 while문 2가지


# import random

# r_num = random.randint(1,100)
# count=0
# #for
# for i in range(10):
#   print(f"{i+1}번쨰도전!!")
#   num=int(input("숫자입력"))
#   if num>r_num:
#     print("숫자가 큽니다. 다시입력하세요")
#   elif num<r_num:
#     print("숫자가 작습니다. 다시입력하세요")
#   elif num==r_num:
#     print("정답입니다.")
#     count=1
#     break
# if count==0:
#   print("10번도전에 실패하였습니다. 정답은",r_num,"입니다")

# #while
# i=0
# while i<10:
#    print(f"{i+1}번째 도전!")
#    num=int(input("숫자입력"))
#    if num>r_num:
#     print("숫자가 큽니다. 다시입력하세요")
#    elif num<r_num:
#     print("숫자가 작습니다. 다시입력하세요")
#    elif num==r_num:
#     print("정답입니다.")
#     count=1
#     break
#    i+=1
# if count==0:
#   print("10번도전에 실패하였습니다. 정답은",r_num,"입니다")
 

#1~100 까지의 랜덤숫자를 생성
#입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
#입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
#10번 도전하기 정답을 맞추면 정답입니다. 프로그램 종료 break
# 10번 도전에  실패할경우
#for문 while문 2가지

students =[
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]
#   #찾는 학생이 있으면 찾는 학생이름이 있습니다, 없으면 찾는 학생이름이 없습니다.
#   #합계 평균추가
search = input("학생이름")
count=0
for s in students:
  if s[1]==search:
    print("학생이 있습니다.")
    count=1
    break
if count==0:
  print("학생이 없습니다.")

for s in students:
  s.append(s[2]+s[3]+s[4])
  # s.append("{:.2f}".format((s[2]+s[3]+s[4])/3))
  s.append(f"{((s[2]+s[3]+s[4])/3):.2f}")
print(students)