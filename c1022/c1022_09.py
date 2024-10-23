# #문자열,리스트 슬라이싱 가능함
# a = "안녕하세요."
# print(a[1:])
# print(a[1:-1])
# print(a[:3])
# print(a[::-1])

# list = [1,2,3,4,5,6,7,8,9]
# print(list[1:-1])




# a = ""
# print(a)
# print("완료")
# #print(int(a)) #에러
# print("완료")

# 정렬
n_lists = [
  ["john",100,4.5,1000],
  ["park",80,4.2,800],
  ["lee",90,4.4,2000],
  ["trumf",200,4.7,10],
  ["bill",30,4.3,30]
]

print("기본 :",n_lists)
# n_lists 에서 1개(n_list) x대입
n_lists.sort(key=lambda x:x[0],reverse=True)
print("이름정렬 :", n_lists)

