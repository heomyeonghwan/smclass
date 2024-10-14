# def gugudan(n1,n2):
#   for i in range(n1,n2+1):
#     print(f"[{i}단]")
#     for j in range(1,10):
#       print(f"{i}*{j}={i*j}")

# # 구구단을 출력
# #2단에서 5단
# gugudan(2,5)

  
# #3단~9단
# gugudan(3,9)


# #5단~8단
# gugudan(5,8)



# def gugudan(n):
#   for i in range(2,n+1):
#     print(f"[{i}단]")
#     for j in range(1,10):
#       print(f"{i}*{j}={i*j}")

# nArr = [9,5,7]
# ##2~9 2~5 2~7
# # gugudan(9)
# # gugudan(5)
# # gugudan(7)

# for i in nArr:
#   gugudan(i)
#   print("-"*50)


subName = ['국어','영어','수학']
score = {"국어":100,"영어":95,"수학":80}
print(score)
print(score['국어'])
print(subName[0])
print(score[subName[0]])

for i in subName:
  print(i,":",score[i])
  
for k,v in score.items():
  print(k,":",v)