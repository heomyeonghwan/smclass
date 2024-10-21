# input_str = input("글자를 입력하세요.")

# #문자가 입력되지않았을때
# if input_str=="":
#   print("글자를 입력하셔야합니다.")
# else:
#   print("입력문자: ",input_str)
#   print("프로글램이 종료됩니다.")

# if input_str !="": #빈공백이 아니냐
#   print("입력문자: ",input_str)
#   print("프로글램이 종료됩니다.")
# else:
#   print("글자를 입력하셔야합니다.")

#####문자열####
#문자열 숫자
a="123"
print(type(a)) #str 
print(type(int(a))) #int
print(type(float(a))) #float
b="12.6"
# print(type(int(b))) #에러, 소수점이 있는 문자열숫자는 float으로 변경해야함
print(type(float(b))) #float
c=12.3
print(type(int(c))) #실수는 int타입으로 변경가능
print(int(c))
#문자열 연결연산자
s1="안녕"
s2="하세요"
print(s1+s2)
print(a+b) #문자열 연결연산자 +
#print(a*b)#에러: 문자열은 ,*,/ 안됨

#문자열 *2
print("안녕"*10) #문자열 반복연산자
print("-."*30)
      
#문자열 슬라이싱
str1 = "안녕하세요.반갑습니다." #문자열자체 - 리스트 형태
print(str1[0]) #해당번호 입력 > 해당되는 문자출력
print(str1[6])
print(str1[2:5]) #해당범위 출력  [범위시작점:범위끝점 한칸뒤]
print(str1[:5]) #해당범위 출력  [처음:범위끝점 한칸뒤]
print(str1[2:]) #해당범위 출력  [범위시작점:끝까지]
print(str1[1:10:2]) #해당범위 출력  [범위시작점:범위끝점 한칸뒤:칸 띄우기]
print(str1[1:10:3]) #해당범위 출력  [범위시작점:범위끝점 한칸뒤:칸 띄우기]
print(str1[::-1]) #해당범위 출력  [범위시작점:범위끝점:역순]

#[] - 배열: 범위가 한번 정해지면 수정불가
#[] - 리스트: 범위 상관없음.