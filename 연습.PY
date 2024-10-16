stu_key=["no","name","kor","eng","math","total","avg","rank"]
students=[]
# 파일읽기 - r
f = open('a.txt','r',encoding='utf-8')

while True:
  line = f.readline()
  if not line:break
  print(line.strip())