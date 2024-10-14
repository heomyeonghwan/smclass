#
import random
fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry",
         "파인애플":"pineapple","코코넛":"coconut"}

# fName = ["바나나","오렌지","체리","파인애플","코코넛"]
fName = list(fruit.keys())
print(list(fruit.keys()))

# #바나나를 입력하면 영어로 출력
# print(fruit["바나나"])
# print(fruit["오렌지"])

# while True:
#   search = input("과일이름을 입력하세요.>>")
#   if search in fruit:
#     print("영문으로 : ",fruit[search])
#   else:
#     print("없습니다.")




# #1
# search = input("바나나의 영문을 입력하세요.>>")
# if fruit["바나나"]==search:
#   print("정답입니다.",fruit["바나나"],search)
# else:
#   print("오답입니다.",fruit["바나나"],search)


# #2 fName 순서대로 영단어 맞추기
# print("[영단어 맞추기]")
# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요.>>")
#   if fruit[key]==search:
#     print("정답입니다.",fruit[key],search)
#   else:
#     print("오답입니다.",fruit[key],search)

# #3 fName 랜덤순서로 영단어 맞추기
# # random.shuffle(fName) #원본이 변경이 됨
# re_fName = random.sample(fName,5)
# #print(re_fName)
# for i in re_fName:
#   search = input(f"{i}의 영문을 입력하세요.>>")
#   if fruit[i]==search:
#     print("정답입니다.",fruit[i],search)
#   else:
#     print("오답입니다.",fruit[i],search)