import os

f = open("b1017/students.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  print(line.strip())



# if os.path.exists("b1017/students.txt"):
#   print("파일이 존재합니다")
# else:
#   print("파일이 존재하지않습니다.")
