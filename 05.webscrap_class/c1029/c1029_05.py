# a = 1
# b = 2 
# a_list = [a,b]
# print(a_list)
# print(type(a_list))

# b_list= [b]
# print(type(b_list))


# #튜플을 1개만 지정할때 뒤에 , 를 넣어야한다
# a_tuple = (a,b)
# print(type(a_tuple))

# #b_tuple = (a) #int타입
# b_tuple = (a,) #tuple타입
# print(type(b_tuple))

# select * from employees where emp_name like '%a%';

# name = '홍길동'
# #문자변수
# print('안녕하세요. 이름은%s'%name)
# #format 함수
# print('hello. my name is {}'.format(name))
# #문자 f함수
# print(f'hello. my name is {name}')



#딕셔너리로 만들어 넣기
# title = ['e_id','e_name','salary']
# a = [192, 'Sarah Bell', 4000.0]
# print(type(a))

# print(dict(zip(title,a)))


#딕셔너리로 만들어 넣기
title = ['e_id','e_name','salary']
aa = [
(196, 'Alana Walsh', 3100.0),
(125, 'Julia Nayer', 3200.0),
(180, 'Winston Taylor', 3200.0),
(194, 'Samuel McCain', 3200.0),
(138, 'Stephen Stiles', 3200.0)
]
a_list=[]

for i in aa:
  a_list.append(dict(zip(title,i)))
print(a_list)

aa_list = list(map(dict(zip(t,i))))