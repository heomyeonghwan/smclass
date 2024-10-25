# #리스트 + 리스트
# a = [1,2,3]
# b = [4,5,6,7]
# print(a+b)


# #
# a = '1.7만'
# if '만' in a:
#   print("있다")
# else:
#   print("없다")


#float 타입으로 변경해서 리스트로 저장 
#내가
a = ['1만','3,450','1.7만','500','1,000']
b = []
for i in a:
  if '만' in i:
    s = (float(i[:-1])*10000)
    b.append(s)
  else:
    s = (float(i.replace(",","")))
    b.append(s)
print(b)

#float 타입으로 변경해서 리스트로 저장 
def chg(val):
  r_val = 0
  if '만' in val:
    r_val = float(val[:-1])*10000
  else:
    r_val = float(val.replace(",",""))
  return r_val

a_list = list(map(chg,a))
print(a_list)

#최대값
print(max(a_list))
#최소값
print(min(a_list))
#역순정렬
a_list.sort(reverse=True)
print(a_list)                        