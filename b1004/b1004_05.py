# #구구단을 입력한 단까지 출력
# n = int(input("단을 입력"))
# for i in range(1,n+1):
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#    print(f"{i}x{j}={i*j}")
#   print("-"*50)

# #입력한 단만 출려
# n = int(input("단을 입력"))
# for i in range(n,n+1):
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#    print(f"{i}x{j}={i*j}")
#   print("-"*50)

#000
#001
#...
#997
#998
#999

# #for 3번사용
# for i in range(0,9+1):
#   for j in range(0,9+1):
#     for k in range(0,9+1):
#       print(f"{i}{j}{k}")

# #for 1번사용
# for i in range(1000):
#   print(f"{i:03d}")


## for문을 출력
## 가로출력
# for i in range(2,10):
#   print(f"[{i}단]")
#   for j in range(1,10):
#     print(f"{i}x{j}={i*j}",end=" ")
#   print()

##세로출력
for k in range(1,10):
  print(f"[{k}단]",end="\t")
print()
for i in range(1,10):
  for j in range(1,10):
    print(f"{j}x{i}={j*i}",end="\t")
  print()