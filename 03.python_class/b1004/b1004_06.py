####enumerate()함수##
# a_list=['홍길동','유관순','이순신','강감찬','김구','김유신','홍길자']
# #for 문으로 출력
# for a in a_list:
#   print(a)
# print("-"*50)
# #enumerate()함수 - index번호를 출력 index,value
# for i,a in enumerate(a_list):
#   print(f"{i}:{a}")

# print(a_list)

# ###
# a_list = [1,2,3,4,5]
# #b_list = [1*1,2*2,3*3,4*4,5*5]

# print(a_list)

# #리스트의 값을 변경해서 리스트에 저장1
# # for idx,a in enumerate(a_list):
# #   a_list[idx] = a**2
# ##  a_list[idx] = a+2

# #리스트의 값을 변경해서 리스트에 저장2- 리스트 내포,한줄 for문
# a_list = [a**2 for a in a_list]
# #a_list = [a+2 for a in a_list]
# print(a_list)



a_list=['홍길동','유관순','이순신']
#뒤에 님을 붙여 다시 저장
a_list=[a+'님' for a in a_list]
print(a_list)



# #리스트 값변경
# print(a_list)
# a_list[1] = 100
# print(a_list)

# #list 슬라이싱 - 0부터 4앞까지 출력(3)
# print(a_list[0:4])
# #list 범위보다 넘어서 출력하면 에러가 나지않고 출력은 가능(범위까지만 출력)
# print(a_list[0:10])

# #없는 list위치에 값을 수정할수없다
# a_list[5] = 1000 
# print(a_list)
#없는 list위치를 출력할수없다
#print(a_list[10])


