from django.shortcuts import render,redirect
from member.models import Member


# 로그인 페이지 ,로그인 확인
def login(request):
  if request.method == "GET":
    return render(request,"login.html")
  else:
    id = request.POST.get("id","")
    pw = request.POST.get("pw","")
    print("확인:",id,pw)

    # db 에 id,pw 있는지 확인, 있으면 로그인, 없으면 다시 로그인
    qs = Member.objects.filter(id=id,pw=pw) # filter : 검색
    
    if qs:
      print("id,pw가 존재합니다.")
      loginmsg = "1"
      request.session["session_id"] =qs[0].id
      request.session["session_nicName"] =qs[0].nicName
    else:
      print("id,pw가 존재하지 않습니다.")
      loginmsg = "0"

    context = {"loginmsg":loginmsg}
    return render(request,'login.html',context)


# 로그아웃
def logout(request):
  request.session.clear()
  print("확인 : session 삭제")
  return redirect("/")