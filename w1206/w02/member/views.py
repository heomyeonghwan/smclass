from django.shortcuts import render,redirect
from member.models import Member
# 

def login(request):
  if request.method == "GET":
    return render(request,'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")

    qs= Member.objects.filter(id=id,pw=pw)
    
    
    if qs:
      print("아이디 패스워드가 존재합니다.")
      lmsg = "1"
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName

    else:
      print("아이디 패스워드가 존재하지않습니다.")
      lmsg = "0"

    context = {"lmsg":lmsg}

    return render(request,'login.html',context)


#

def logout(request):
  request.session.clear()
  print("session 삭제")
  return redirect("/")