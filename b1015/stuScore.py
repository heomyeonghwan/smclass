# import S_func/ ##함수앞에 S_func 붙여줘야함
from S_func import * ##모든함수 가져오기
#from S_func import title_program() ##하나씩가져오기


# 학생성적프로그램
while True:
  choice = title_program()        # 메뉴출력함수 호출
  if choice == "1":
    stuNo = stu_input(stuNo)                   # 학생성적입력함수 호출
  elif choice == "2":
    stu_output(students)                # 학생성적출력함수 호출
  elif choice == "3":
    stu_update(students)                  # 학생성적수정함수 호출
  elif choice == "4":
    stu_select(students)                 #학생성적검색함수 호출
  elif choice == "5":
    stu_delete(students)                    #학생성적삭제함수 호출
  elif choice == "6":
    stu_rank(students)                    #학생성적등수처리 함수 호출
  elif choice == "7":
    stu_sort(students)                   #학생성적정렬 함수 호출
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break


























