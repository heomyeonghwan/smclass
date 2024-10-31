import random
import oracledb
import smtplib
from email.mime.text import MIMEText

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

# 시작화면 함수선언
def screen():
  #로그인이 되어있지 않은 상태
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>> ")

  return choice

#1. 로그인 함수선언
def memLogin():
  print("[ 로그인 ]")
  user_id = input("아이디를 입력하세요.>> ")
  user_pw = input("패스워드를 입력하세요.>> ")
  # db접속
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id=:id and pw=:pw"
  cursor.execute(sql,id=user_id,pw=user_pw) #날리기
  row = cursor.fetchone() #1개 받아오기
  cursor.close() # close되면 다시 커서 커넥트해야함
  if row == None:
    print("아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요!! ") 
    return #함수일때는 continue 말고 returnTma

  #이후 프로그램 구성
  print(f"{row[2]} 님 환영합니다.")
  print()


#임시비밀번호 생성 함수선언
def random_pw():
  a = random.randrange(0,10000)# 0-9999
  ran_num = f"{a:04}"
  print("랜덤번호 : ",ran_num)
  return ran_num


#메일발송 함수선언
def emailSend(email):
  # email 발송관련
  smtpName = "smtp.naver.com"
  smtpPort = 587

  # 자신의 네이버메일주소,pw, 받는사람이메일주소
  sendEmail = "gopsl3957@naver.com"
  pw = "MELODIES00"
  recvEmail = email

  title = "제목 : [ 메일발송 ] 임시번호 안내"

  ##랜덤함수없이하기
  # a = random.randrange(0,10000)# 0-9999
  # ran_num = f"{a:04}"
  # print("랜덤번호 : ",ran_num)

  #랜덤함수이용
  ran_num = random_pw()
  content = "임시비밀번호 :"+ran_num # content 보낼내용
  print(content)

  #설정
  msg = MIMEText(content)
  msg['Subject'] = title
  msg["From"] = sendEmail
  msg['To'] = recvEmail
  
  # 서버이름,서버포트
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendEmail,pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  s.quit()

  # 메일발송 완료
  print("메일이 발송되었습니다.")

  return ran_num

#2. 비밀번호 찾기 함수선언
def search_pw():
  print("[ 비밀번호 찾기 ]")
  search = input("해당 아이디를 입력하세요.>> ")
  # 아이디 있는지 확인
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id=:id"
  cursor.execute(sql,id=search)
  row = cursor.fetchone()

  if row == None:
    print("아이디가 존재하지않습니다. 다시입력하세요!")
    return #함수일때는 continue 말고 returnTma

  input(f"{row[0]} 아이디가 존재합니다. 메일을 보내려면 ENTER를 입력하세요.")

  #이메일 발송함수 호출
  ran_num = emailSend(row[3])

  #임시비밀번호를 update
  sql = "update member set pw=:pw where id=:id"
  cursor.execute(sql,pw=ran_num,id=search)
  conn.commit()
