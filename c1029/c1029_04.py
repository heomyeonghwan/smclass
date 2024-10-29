# employees 테이블에서 이름이 a 가 포함되어있는 이름, 모든 컬럼 출력
import oracledb

#db 연결 함수호출
def connections():
  try:
    conn = oracledb.connect(user = 'ora_user', password= '1111', dsn='localhost:1521/xe')
    print("db연결: ",conn.version)
  except Exception as e: print("예외발생:",e)
  return conn

#함수호출
conn = connections()
cursor = conn.cursor()

#범위를 입력받아 그사이 사원을 정렬해서 출력
num1 = input("범위를 시작점입력")
num2 = input("범위를 마지막점입력")

sql = "select employee_id,emp_name,salary from employees where salary >= :num1 and salary <=:num2 order by salary"
cursor.execute(sql,num1=num1,num2=num2)


# #월급이 4000~8000사이의 사원을 모두출력
# sql = "select employee_id,emp_name,salary from employees where salary >= 4000 and salary <=8000"
# cursor.execute(sql)





# #3. 입력한 값이 이름에 포함되어있는 데이터를 출력
# search = input("검색할 이름을 입력하세요>>")
# search = '%'+search+'%'
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)




# 2. search = input("번호검색>>")

# #키워드 검색
# sql = "select * from employees where employee_id>=:search"
# cursor.execute(sql,search=search)
# #번호순서
# sql = "select * from employees where employee_id>=:1"
# cursor.execute(sql,[search])



# #1.employees 테이블 emp_name a 가 포함되어있는 row모두 출력하시오

# sql = "select * from employees where emp_name like '%a%'"
# cursor.execute(sql)



title = ['employee_id','emp_name','salary']
a_list = [] #dict 타입으로 변경해서 저장하시오

rows = cursor.fetchall()
for row in rows:
 a_list.append(dict(zip(title,row)))
 print(row)
print(a_list)

conn.close()