students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

#합계 평균 추가해서 전체를 출력하시오
#1 홍길동 100 90 99 289 92.00
print("번호\t번호\t번호\t번호\t번호\t번호\t번호")
print("-"*55)
for s in students:
  s.append(s[2]+s[3]+s[4])
  s.append(f"{((s[2]+s[3]+s[4])/3):.2f}")
  print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}")