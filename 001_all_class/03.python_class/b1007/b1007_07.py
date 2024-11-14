import random
lotto = [0]*6+[1]*3
random.shuffle(lotto)
print(lotto)
a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

for i in range(3):
  for j in range(3):
    a_list[i][j]=lotto[3*i+j]
 


aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

print(a_list)
while True:
  my_money = int(input("얼마를 투자하시겠습니까?>>"))

  print("         [i,j 좌표]")
  print("\t0\t1\t2")
  print("-"*30)
  for i in range(3): ##i >[1,2,3,]
    print(i,"|",end="\t")
    for j in range(3): ## j > 1
      print(aa_list[i][j],end="\t")
    print()
  code = input("좌표를 입력하세요.(0.0)>.")
  codeArr = code.split(".") ##codeArr[0],codeArr[1]
  #print(codeArr)
  print(f"{codeArr} 좌표값: ",a_list[int(codeArr[0])][int(codeArr[1])])
  a = a_list[int(codeArr[0])][int(codeArr[1])]
  if a == 1:
    aa_list[int(codeArr[0])][int(codeArr[1])] = '당첨'
    print(f"{codeArr} 당첨금 : {my_money*10:,d}")
  elif a ==0:
    aa_list[int(codeArr[0])][int(codeArr[1])] = '꽝'
    print(f"{codeArr}다음기회에 : {my_money}")