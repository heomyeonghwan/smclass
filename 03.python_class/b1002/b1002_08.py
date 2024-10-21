###리스트 if
##in - 데이터가 있는지 확인
##count - 데이터 개수
##find - 데이터가 있는위치, 없으면 -1  , find(검색어,시작위치,끝위치)
##index - 데이터가 있는위치, 없으면 에러


# fruit =['사과','배','딸기','포도','배']
# if '배' in fruit:  #1번의 비교로 있는지 확인
#   print("배가 있음")
# else:
#   print("배가없음")

# fruit ="사과,배,딸기,포도"
# if '배' in fruit:
#    print("배가 있음")
# else:
#    print("배가없음")

# fruit =['사과','배','딸기','포도','복숭아']
# #글을 입력받아 입력한 과일이있으면 있음, 없으면 없음 출력
# name = input("과일입력")
# if name in fruit:
#   print(name,"이(가) 있어요")
#   #print(f"{name}이(가) 있어요")
# else:
#   print(name,"이(가) 없어요")

# #count >리스트에서 개수 확인
# fruit =['사과','배','딸기','포도','복숭아','배','사과','배','딸기']
# print(fruit.count('배'))
# print(fruit.count('사과'))

# #count >문자열 내에 해당 숫자수 확인
# fruit ="사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# print(fruit.count('사과'))

# #과일이름을 입력받아 있으면 있다 > 과일검색개수:, 없으면 없습니다
# name = input("과일입력")
# if name in fruit:
#   print(f"{name}이(가) 있습니다.")
#   print("과일검색개수: ",fruit.count(name))
#   print(fruit.find(name))
#   #print(fruit.index(name)) # name 이 있는지 위치에 index
# else:
#   print(f"{name}이 없습니다.")
#   print(fruit.find(name))
#  # print(fruit.index(name)) # name 이 있는지 위치에 index 없으면 에러
        
fruit ="사과,배,딸기,포도,복숭아,배,사과,배,딸기"
#배가 있는 위치를 모두 출력
search = input("과일이름을 입력하세요")
print("모든 과일",search)
idx = 0
if fruit.count(search)>0:
  print(f"{search}글자가 있습니다")
  for i in range(fruit.count(search)):
      print(f"{search}가있는위치:",fruit.find(search,idx))  #find(찾을문자, 시작index, 끝index)
      idx = fruit.find(search,idx)+1
else:
  print(f"{fruit}는 없습니다")
  