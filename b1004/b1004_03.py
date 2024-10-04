###파이썬 - 문자열(str) 정수형(int) 실수형(float) 논리형(bool)
###for 문
#range() 범위
#0부터 1씩 증가하면서, 10번 실행(0-9)
for i in range(10):
  print(i)
print("-"*50)
#5부터 10 이전까지 5번 실행(5-9)
for j in range(5,10):
  print(j)
print("-"*50)

a_list=[1,2,3,4,5]
for k in a_list:
  print(k)
print("-"*50)
#리스트타입
b_list=[3,5,9,10,20,3,3,10,5,20]
for n in b_list:
  print(n)
print("-"*50)

#딕셔너리 타입- {키,값(key,value)}:json타입과 모양이 같음. 
dic = {
  "번호":1,"이름":"홍길동","국어":100,
  "영어":100,"수학":99
}
print(dic["번호"])
print(dic["이름"])
for m in dic: #dic에서 key 값을 m에 넣어줌
 # print(m) #key 값이 출력이됨
  print(dic(m))   #key값의 value값이 출력이됨
print("-"*50) 

#list길이 : len()
print(len(b_list))
print("-"*50)

#리스트 안에 해당되는 숫자가 몇개인지 확인 - count
print(b_list.count(3))
print(b_list.count(5))
print("-"*50)

#리스트 추가 -append, insert, extend([2,3])-리스트 여러개 추가
#리스트 삭제 -del, remove, clear(모두삭제)