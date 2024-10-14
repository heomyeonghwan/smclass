import random
a_list=[]
for i in range(25):
  a_list.append(i+1)
print(a_list)
random.shuffle(a_list)
print(a_list)
b_list=[]
# for i in range(5):
#   a=[]
#   for j in range(5):
#     a.append(a_list[(5*i+j)])
#   print(a)
#   b_list.append(a)
# print(b_list)
for i in range(0,25,5):
  b_list.append(a_list[i:i+5])
print(b_list)

print()
print("\t0\t1\t2\t3\t4")
print()
print("-"*60)
for i in range(5):
  print(i,"|",end="\t")
  for j in range(5):
    print(b_list[i][j],end="\t")
  print()
