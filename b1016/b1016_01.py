





### 파일읽기 - r
#위치에 파일이 업으면 에러


# # #절대경로를 사용해서 파일을찾음
# # f = open('c:/aaa/a.txt','r',encoding='UTF-8') ### encoding='UTF-8' >>한글을 가지고옴
# # #가장 바깥 폴더의 위치에서 파일을 찾음
# # f = open('a.txt','r',encoding='UTF-8') ### encoding='UTF-8' >>한글을 가지고옴

## 1.  readline() - 1줄씩 읽어오기
# f = open('a.txt','r',encoding='UTF-8') ### encoding='UTF-8' >>한글을 가지고옴
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip()) ## strip(): \n 값을 생략
# f.close()



# ## 2. readlines() - 모든글 읽어오기(리스트 타입으로 읽어옴)
# f = open('a.txt','r',encoding='UTF-8')
# lines = f.readlines()
# print(lines)
# for line in lines:
#   print(line.strip())
# f.close()



# ## 3. read() - 1줄씩 읽어오기
# f = open('a.txt','r',encoding='UTF-8')
# #print(type(f))
# for line in f:
#   print(line.strip())
# f.close()


###### 파일쓰기 -w : 파일 생성 후 글자 입력// 글자 누적안됨 > 덮어씀

# f = open('aa.txt','w',encoding='UTF-8')
# f.write("안녕하세요.1 \n")
# f.write("안녕하세요.2 \n")
# f.write("안녕하세요.3 \n")
# f.close()
# print("글쓰기 종료")


# f = open('aa.txt','w',encoding='UTF-8')
# for i in range(1,11):
#   data = f"안녕하세요. {i}\n"
#   f.write(data)
# f.close()
# print("글쓰기 종료")

# while True:
#   print("[메모장]")
#   data = input("저장하려는 글자를 입력하세요.>>")
#   f = open("aa.txt","w",encoding='UTF-8')
#   f.write(data)
#   f.close()

####### 파일 이어쓰기 - a

# while True:
#   print("[메모장]")
#   data = input("저장하려는 글자를 입력하세요.>>")
#   f = open("aa.txt","a",encoding='UTF-8')
#   f.write(data+"\n")
#   f.close()

#   ######### 파일 with > close()를 하지 않아도됨
# with open("aa.txt","w",encoding='UTF-8') as f:
#   f.write("안녕하세요.")