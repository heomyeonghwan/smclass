import random

# # a =1
# # print(f"{a:04}")
# # #print("{}".format(a))

# #임시비밀번호 생성
# a_list = [0,1,2,3,4,5,6,7,8,9]
a = random.randrange(0,10000) #0 ~9999

ran_num = f"{a:04}"
#랜덤4자리 숫자
print(ran_num)



# ##### 비밀번호 수정하는거
# import oracledb

# def connects():
#   user="ora_user"
#   password = "1111"
#   dsn = "localhost:1521/xe"
#   try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
#   except Exception as e: print("예외발생 : ",e)
#   return conn

# # db접속
# conn = connects()
# cursor = conn.cursor()

# #입력
# user_id = input("아이디를 입력하세요.>> ") #eee
# user_pw = input("패스워드를 입력하세요.>> ") #2222

# #데이터 수정
# sql = "update member set pw=:pw where id=:id"
# cursor.execute(sql,id=user_id,pw=user_pw)
# conn.commit()

# print("파일이 수정되었습니다.")
# cursor.close()