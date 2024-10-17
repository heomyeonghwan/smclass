

a = ['20', 'sgrinyakinj', '75', '64', '72', '211', '70.3333333333', '1']
b = ['20', '75', '64', '72', '211', '70.3333333333', '1']
t_title = ['no','name','kor','eng','math','total','avg','rank']
students =[]
c = []

# # b의 리스트를 float으로 변경
# # b의 형태가 모두 숫자 > float변경가능
# for i in b:
#   c.append(float(i))
# print(c)


# ####try-except 구문을 사용해서 정수, 실수 구분
# def t_float(n):
#   try:
#     int(n)
#     return True
#   except:
#     return False
  
# #정수로 변경
# for i in b:
#   if t_float(i):
#     i = int(i)
#   else:
#     i = float(i)
#   c.append(i)
# print(c)

# #문자열인지 아닌지 구분
# for idx,i in enumerate(a):
#   if i.isdigit():
#     print(f"{idx}번째 {i}는 숫자입니다.")
#   else:
#     print(f"{idx}번째 {i}는 문자입니다")


###
def f_float(value):
  if value.isdigit(): ##1. 정수인지, 2. 실수나 문자열인지  2가지로 판별
    return int(value)
  else:
    try:
      return float(value) ##실수일때 실수로 변환 리턴
    except:
      return value #문자열일때 문자열 그대로 리턴

##문자열,정수,실수 구성
c=[]
for idx,value in enumerate(a):
  c.append(f_float(value))

#students 리스트에 딕셔너리로 저장
students.append(dict(zip(t_title,c)))  
print(students)

#b는 숫자로만 구성 - 정수,실수
for idx,value in enumerate(b):
  if value.isdigit(): #isdigit -정수:True, 실수:False
    print(f"{idx}번째 {type(int(value))}")
  else:
    print(f"{idx}번째 {float(value)}")
