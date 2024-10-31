import func


while True:
  #시작화면 출력
  choice = func.screen()

  #로그인 부분
  if choice == "1":
    func.memLogin()

  #비밀번호 찾기 부분
  elif choice == "2":
    func.search_pw() #함수 위치 컨트롤 클릭하면 찾음
  #회원가입 부분
  elif choice == "3":
    print("[ 회원가입 ]")




  elif choice == "0":
    print("프로그램 종료합니다.")
    break