import oracledb
import stu_func


while True:
  choice = stu_func.main_print()   ## 메인화면출력부분
  if choice == "1":
    stu_func.stu_insert()          ## 학생성적입력부분
  elif choice == "2":
    stu_func.stu_output()          ## 학생성적출력부분  
  elif choice == "3":
     stu_func.stu_select()         ## 학생성적검색부분
  elif choice == "4":
    stu_func.stu_sort()            ## 학생성적정렬부분
  elif choice =="5":
    stu_func.stu_rank()            ## 등수처리 부분
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break




