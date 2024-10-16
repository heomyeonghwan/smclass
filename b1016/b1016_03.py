
stu_key=["no","name","kor","eng","math","total","avg","rank"]
students=[]
# 파일읽기 - r
f = open('a.txt','r',encoding='utf-8')

while True:
  line = f.readline()
  if not line:break
  s = line.strip().split(",")
  
  s[0] = int(s[0]) ### 위 포문이랑 같음
  s[2] = int(s[2])
  s[3] = int(s[3])
  s[4] = int(s[4])
  s[5] = int(s[5])
  s[6] = float(s[6])
  s[7] = int(s[7])


  students.append(dict(zip(stu_key,s)))
  print(line.strip())
f.close()
print(students)



## 합쳐서 딕셔너리 형태로 만들기
# a=["홍길동","유관순","이순신"]
# b=[100,90,80]
# c=zip(a,b)
# #print(list(c))
# print(dict(c))

# #
# a=["no","name","kor","eng"]
# b=[1,'홍길동',100,90]
# print(dict(zip(a,b)))