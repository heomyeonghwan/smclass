import oracledb

#db연결 함수선언
def connects():
  user='ora_user'
  password='1111'
  dsn = 'localhost:1521/xe'
  try:
    conn=oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외처리",e)
  return conn

##회원수 확인
def member_count():
  ## oracle db - mem 테이블의 count를 가져오시오
  conn = connects()
  cursor = conn.cursor()
  ###employees 테이블 부서번호 50번인 사원수를 가져오시오.
  sql = "select count(department_id) from employees where department_id =50"
  cursor.execute(sql) #날리기
  row = cursor.fetchone() #
  print(row)
  cursor.close() # close되면 다시 커서 커넥트해야함
  return row
  

###회원수 확인값을 리턴하시오.
all_member = member_count()
#all_member = 100

print("[ 커뮤니티 ]")
print(f"현재 회원수: {all_member[0]},부서번호: {all_member[1]},부서명: {all_member[2]}")
print()
print("1. 로그인")
print("1. 회원가입")
print("1. 회원정보수정")
choice = input("원하는 번호를 입력하세요.>>")

if choice == "1":
  pass




# # db접속
# conn = connects()
# cursor = conn.cursor()
# sql = "select * from member where id=:id and pw=:pw"
# cursor.execute(sql,id=user_id,pw=user_pw) #날리기
# row = cursor.fetchone() #1개 받아오기
# cursor.close() # close되면 다시 커서 커넥트해야함