stu_data = ['홍길동',100,100,100,99]

# for s in stu_data:
#   print(s)

  
# stu_datas = [['유관순',100,100,100,99],['이순신',100,99,98,99],['김구',80,100,90,99]]
# #학생데이터에서 합계,평균을 추가해서 1줄로 출력하시오
# for s in stu_datas:
#   print("{},{},{},{},{},{},{:.1f}".format(s[0],s[1],s[2],s[3],s[4],(s[1]+s[2]+s[3]+s[4]),((s[1]+s[2]+s[3]+s[4])/4)))


stu_title =['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [[1,'유관순',100,100,100,99],[2,'이순신',100,99,98,99],[3,'김구',80,100,90,99]]
 #학생데이터에서 합계,평균을 추가해서 1줄로 출력하시오
# print("                                [학생성적 프로그램]")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7]))
# print("-"*60)


# #학생데이터에서 합계,평균을 추가해서 1줄로 출력하시오. 2
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("-"*60)

for s in stu_datas:
 print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],(s[2]+s[3]+s[4]+s[5]),((s[2]+s[3]+s[4]+s[5])/4)))


# #이순신의 평균 출력
# print(stu_datas[1][0],"의 평균:",(stu_datas[1][1]+stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4])/4)

# #학생이름: 홍길동
# #국어:100
# #영어:100
# #수학:100
# #과학:99
# #합계:
# #평균:

# print("학생이름:",stu_data[0])
# print("국어:",stu_data[1])
# print("영어:",stu_data[2])
# print("수학:",stu_data[3])
# print("과학:",stu_data[4])
# print("합계:",stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4])
# print("평균:{:.1f}".format((stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4])/4))



# #한번에 두개의길이를 입력받아, 삼각형의 넓이 직사각형의 넓이를 구하시오.
# leg = input("두개의 길이를입력")
# print(leg.split(" "))
# l_list = leg.split(" ")
# print("삼각형의 넓이:{}".format(float(l_list[0])*float(l_list[1]))/2)
# print("사각형의 넓이:{}".format(float(l_list[0])*float(l_list[1])))

# a=int(input("가로를입력"))
# b=int(input("세로를입력"))

# print("삼각형의 넓이:",a*b/2)
# print("사각형의 넓이:",a*b)


# #원의넓이 : 반지름*반지름*3.14
# #반지름을 입력받아 원의 넓이를 구하시오

# r = int(input("반지름의 넓이를 입력"))
# area = r**2*3.14
# print("원의넓이:",area)
# print("원의넓이:{:.1f}".format(area))


# ##복합대입연산자 +=,-=,*=,/=,%=,//=,**=
# a=10
# a+=5; print(a)
# a-=5; print(a)
# a*=5; print(a)
# a/=5; print(a)
# a//=5; print(a)
# a**=5; print(a)
# a%=5; print(a)


# ### 숫자를 문자열로 변환
# #문자열 + 숫자열 : 변환X
# a=100
# b=10
# print(str(a)+str(b))


###문자형 숫자 변환
# a= "100"
# b= "10.5"
# print(float(a)) # 정수형 문자열 > 정수,실수타입 변경가능
# #print(int(B))# 에러, 실수형 문자열 > 실수타입으로만 변경가능
# #print(float(c)) # 글자는 숫자형타입으로 변경 불가


# #1줄 선언 방식
# a=10;b=5
# c,d = 10,20
# #1줄 선언 방식
# s1,s2,s3 = 1,2,3


# x=1,2,3,4,5,6,...10
# 1
# x=11,12,13,...20
# 11
# x=21,22,23,...30
# 21


# 특정숫자 a= 0,1,2,3,4,5
# 1,3,5,7,9
# 2x+1


# print(2+2-2*2/2*2)
# print((2+2)-(((2*2)/2)*2))


# a= 5, b =3 # 1줄형태로 표현시 ; 넣어주면됨
# # /,%,//,**
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

# print("{},{},{},{}".format(a/b,a%b,a//b,a**b))