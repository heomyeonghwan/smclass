
###문서파일을 읽기,쓰기,이어쓰기, 내용을 복사해서 쓰기
###txt파일의 내용을 복사
# f = open("students.txt","r",encoding="utf-8")
# ff = open("students2.txt","w",encoding="utf-8")
# while True:
#   line = f.readline()
#   if not line: break
#   ff.write(line)
#   print(line.strip())
# f.close()
# ff.close()

# ##파일(바이너리파일) 자체를 읽어오기
# f = open('1.jpg',"rb")
# fData = f.read()

# f.close()
# print("파일읽기 성공!")

##파일 쓰기 
f = open('1.jpg',"rb")
fData = f.read()
f.close()
print("파일읽기 성공!")
# ff = open('2.jpg','wb')
# len = ff.write(fData)
# print(f"파일 크기 : {len} 바이트")
# ff.close()
ff = open('c:/down/2.jpg','wb') ##파일 자체저장
len = ff.write(fData)
print(f"파일 크기 : {len} 바이트")
ff.close()