from django.shortcuts import render,redirect
from member.models import Member


# 로그인페이지
def login(request):
  if request.method == "GET":
    return render(request,"login.html")
  else:
    id = request.POST.get("id","")
    pw = request.POST.get("pw","")

    print("확인: ",id,pw)

    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      print("id,pw가 존재합니다")
      lmsg = "1"
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName
    else:
      print("id,pw가 존재하지않습니다.")
      lmsg = "0"
    context = {"lmsg":lmsg}
    return render(request,'login.html',context)

# 로그아웃
def logout(request):
  request.session.clear()
  print("확인 : session 삭제")
  return redirect("/")