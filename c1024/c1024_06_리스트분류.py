lists = ['10억','9억5,000','11억5000','7억','12억5,250']

a= '9억 5,000'
#숫자로 변경하는 방법
def num_chg(p):
  b = p.split('억')
  f_num = int(b[0])*100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(",",""))*10000
  else:
    s_num = 0
  price = f_num+s_num
  return price

for li in lists:
  price = num_chg(li)
  print("금액:",price)

print("-"*50)

r_list = list(map(num_chg,lists))
print(r_list)