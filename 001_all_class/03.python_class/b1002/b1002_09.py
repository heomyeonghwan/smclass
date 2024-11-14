fruit ="사과,배,딸기,포도,복숭아,배,사과,배,딸기"

# print(fruit.find("딸기",0)) #5
# print(fruit.find("딸기",fruit.find("딸기",0)+1))  #5+1
# print(fruit.find("딸기",6))

# print(fruit.find("배",0)) #3
# print(fruit.find("배",3+1))
# print(fruit.find("배",fruit.find("배",0)+1)) #15
# print(fruit.find("배",15+1))
# print(fruit.find("배",fruit.find("배",fruit.find("배",0)+1)+1)) 

#리스트인 경우 검색해서 해당되는 index를 출력하시오
#배에 해당되는 index번호를 출력

fruits = fruit.split(",")
print(fruits)
print("전체개수: ",len(fruits))
search = input("검색하려는 과일이름")
for idx,f in enumerate(fruits):
  if f==search:
    print("해당위치: ",idx)