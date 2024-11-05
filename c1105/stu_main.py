import oracledb
import stu_func

s_title=['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

while True:
  choice = stu_func.main_print()
  if choice == "1":
    stu_func.stu_insert()

  elif choice == "2":
    stu_func.stu_output()

  elif choice == "3":
    print("[ 학생성적 검색 ]")
    print("1. 이름으로 검색")
    print("2. 합계순 검색")
    choice = input("원하는 번호를 입력하세요.>>")
    if choice == "1":
      print("[ 학생성적 검색 ]")
      search = input("찾고자하는 이름를 입력하세요.>>")
      search = '%'+search+'%'
      sql="select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')\
          from students where name like :search"
      # db연결
      conn = connects()
      cursor = conn.cursor()
      cursor.execute(sql,search=search)
      rows = cursor.fetchall()
      print("개수:",len(rows))
      for s in s_title:
        print(s,end='\t')
      print()
      print("-"*80)
      if len(rows)<1:
        print("데이터가 없습니다.")
        break
      for row in rows:
        for r in row:
          print(r,end='\t')
        print()
      print()
      print("데이터 출력완료!")
      conn.commit()
      conn.close()

  elif choice == "4":
    print("[ 학생성적정렬 ]")
    print("1. 이름 순차정렬")
    print("2. 이름 역순정렬")
    print("3. 합계 순차정렬")
    print("4. 합계 역순정렬")
    choice = input("원하는 번호를 입력하세요.>>")
    if choice == "1":
      sql="select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')\
          from students order by name asc"
    elif choice == "2":
      sql="select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')\
          from students order by name desc"
    elif choice == "3":
      sql="select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')\
          from students order by total asc"
    elif choice == "4":
      sql="select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd')\
          from students order by total desc"
    #c출력부분
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("개수:",len(rows))
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    if len(rows)<1:
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end='\t')
      print()
    print()
    print("데이터 출력완료!")
    conn.commit()
    conn.close()


  elif choice == "5":
    print("[ 등수처리 ]")
    sql="update students a set rank=(select ranks from\
      (select no,rank() over(order by avg desc) ranks from students)b where a.no = b.no)"
    #출력부분
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("등수처리가 완료되었습니다.")
   #-------------------------------------------------
    
    sql="select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("개수:",len(rows))
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    if len(rows)<1:
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end='\t')
      print()
    print()
    print("등수처리 완료!")
    conn.commit()
    conn.close()


  elif choice == "0":
    print("프로그램을 종료합니다.")
    break



