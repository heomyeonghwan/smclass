
# ##2차원 리스트
# a_list = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]
# # 2차원리스트  > for문을 2번사용
# for i in a_list:
#   for j in i:
#     print(j)


# #[3,3]리스트 [1,2,3],[4,5,6],[7,8,9]
# #for 문을 사용하여 2차원리스트를 만드시오
# a_list=[]
# for i in range(0,3):
#   a = []
#   for j in range(0,3):   ###3x+(y+1)
#     y = 3*i+(j+1)
#     a.append(y)
#   a_list.append(a)
# print(a_list)





# # 1~9까지 리스트에 추가하시오 1차원리스트
# b_list = []
# for i in range(1,10):
#   b_list.append(i)
# print(b_list)

##2차원 리스트
##for문을 2번 삭성해서 1,25 [5,5]리스트를 생성
a_list=[]
for i in range(5):
  a = []
  for j in range(5):
    a.append(5*i+(j+1))
  a_list.append(a)
print(a_list)