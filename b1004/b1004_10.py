s_title= ['번호','이름','국어','영어','수학','합계','평균','등수']
kor = int(input("국어성적을 입력하세요"))
eng = int(input("영어성적을 입력하세요"))
math = int(input("수학성적을 입력하세요"))
print(kor+eng+math)

score = []
for sc in range(3):
  score.append(int(input(f"{s_title[sc+2]}성적을 입력하세요.")))

print(score)