students=[]
s_title=["번호","이름","국어","영어","수학","합계","평균","등수"]
stuNo=1
chk=0
count=1
while True:
    print("[학생성적프로그램]")
    print("-"*60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적검색")
    print("5. 학생성적삭제")
    print("6. 등수처리")
    print("0. 프로그램종료")
    print("-"*60)
    choice = input("원하는 항목의번호를 입력해주세요.>>")
    if choice == "1":
        while True:
            print("[학생성적입력]")
            no=stuNo
            stuNo+=1
            name = input(f"{no}번째 학생의 이름을 입력헤주세요(상위메뉴:0)")
            if name =="0":
                print("성적입력이 종료되었습니다.")
                break
            kor = int(input("국어성적을 입력해주세요."))
            eng = int(input("영어성적을 입력해주세요."))
            math = int(input("수학성적을 입력해주세요."))
            total = kor+eng+math
            avg = total/3
            rank=0
            students.append({
        "no":no,"name":name,"kor":kor,"eng":eng,
        "math":math,"total":total,"avg":avg,"rank":rank
      })
            print(f"{name}학생의 성적이 추가되었습니다")
            for title in s_title:
                print(title,end="\t")
            print()
            print("-"*60)
            for s in students:
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
                print()

    elif choice == "2":
        print("[학생성적출력]")
        for title in s_title:
            print(title,end="\t")
        print()
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
            print()
    elif choice == "3":
        print("[학생성적수정]")
        name = input("수정할 학생의 이름을 입력해주세요>>")
        chk=0
        for s in students:
            if s[1] == name:
                chk=1
                print(f"{name}학생의 성적을 찾았습니다.")
                print("[수정할과목 선택]")
                print("1. 국어성적")
                print("2. 영어성적")
                print("3. 수학성적")
                choice = input("수정할 과목의 번호를 입력해주세요>>")
                if choice == "1":
                    print("수정전 국어성적: ",s[2])
                    s[2] = int(input("변경할 국어성적: "))
                elif choice == "2":
                    print("수정전 영어성적: ",s[3])
                    s[3] = int(input("변경할 영어성적: "))
                elif choice == "3":
                    print("수정전 수학성적: ",s[4])
                    s[4] = int(input("변경할 수학성적: "))
                s[5]=s[2]+s[3]+s[4]
                s[6]=s[5]/3
                print(f"{name}학생 성적이 변경되었습니다.")
                print()
                for title in s_title:
                    print(title,end="\t")
                print()
                print("-"*60)
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
                print()
        if chk ==0:
            print(f"{name}학생이 존재하지않습니다.")        
    elif choice == "4":
        print("[학생성적검색]")
        name = input("검색할 학생의 이름을 입력해주세요>>")
        chk=0
        for s in students:
            if s[1] == name:
                chk=1
                print(f"{name}학생의 성적을 찾았습니다.")
                for title in s_title:
                    print(title,end="\t")
                print()
                print("-"*60)
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
                print()
        if chk == 0:
            print(f"{name}학생이 없습니다.")
    elif choice == "5":
        print("[학생성적삭제]")
        name = input("삭제할 학생의 이름을 입력해주세요")
        chk=0
        for s in students:
            if s[1] == name:
                chk=1
                choice = input(f"{name}학생의 성적을 삭제하시겠습니까?\n1.삭제 2.취소(삭제시 복구불가)")
                if choice =="1":
                    students.remove(s)
                    print(f"{name}학생의 성적이 삭제되었습니다.")
                    print()
                else:
                    print(f"{name}학생 성적 삭제가 취소되었습니다.")
                    print()
        if chk==0:
            print(f"{name}학생이 존재하지않습니다.")
    elif choice == "6":
        print("[등수처리]")
        for s in students:
            count=1
            for st in students:
                if s[5]<st[5]:
                    count+=1
                s[7]=count
        print("등수처리가 완료되었습니다.")
        print()
    elif choice == "0":
        print("[프로그램종료]")
        print("성적처리 프로그램을 종료합니다.")
        break
