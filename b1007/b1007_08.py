import random
lotto = [0]*6+[1]*3
random.shuffle(lotto)
print(lotto)

a_list = []

for i in range(3):
  for j in range(3):
    a_list[i][j] = lotto[3*i+j]

while True:
  print("[i,j좌표]")
  print("\t0\t1\t2")
  print("-"*30)
  for i in range(3):
    for j in range(3):
      print