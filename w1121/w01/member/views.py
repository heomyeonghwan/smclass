from django.shortcuts import render,redirect
from member.models import Member



# 7. 회원정보삭제
def mdelete(request,id):
  print("회원정보:",id)
  Member.objects.get(id=id).delete()
  return redirect('member:mlist')
  # return render(request,"mlist.html") # 다시한번 해야함






# 6. 회원정보수정
def mupdate(request,id):
  if request.method == "GET":
    print("회원정보:",id)
    qs = Member.objects.filter(id=id)
    context = {"mem":qs[0]}
    return render(request,'mupdate.html',context)
  else:
    print("id:",id)
    id = request.session['session_id'] # admin이 아니면 세션을 가지고 저장.
    ## 관리자 로그인이면 id를 가져와서 저장
    if request.session['session_id'] =='admin':
      id = request.POST.get("id")
    
    pw = request.POST.get("pw")
    name = request.POST.get("name")
    nicName = request.POST.get("nicName")
    tel = request.POST.get("tel")
    gender = request.POST.get("gender")
    hobbys = request.POST.getlist("hobby")
    hobby = ','.join(hobbys)

    qs = Member.objects.get(id=id)
    qs.pw = pw
    qs.name = name
    qs.nicName = nicName
    qs.tel = tel
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect("member:mlist")





# 5. 회원정보입력
def mwrite(request):
  if request.method == "GET":
    return render(request,'mwrite.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    name = request.POST.get("name")
    nicName = request.POST.get("nicName")
    tel = request.POST.get("tel")
    gender = request.POST.get("gender")
    hobbys = request.POST.getlist("hobby")
    hobby = ','.join(hobbys)

    Member.objects.create(id=id,pw=pw,name=name,nicName=nicName,tel=tel,gender=gender,hobby=hobby)
    # qs = Member(id=id,pw=pw,name=name,nicName=nicName,tel=tel,gender=gender,hobby=hobby)
    # qs.save()
    return redirect("member:mlist")






# 4. 회원상세
def mview(request,id):
  print("아이디:",id)
  qs = Member.objects.filter(id=id)
  context = {"mem":qs[0]}
  return render(request,'mview.html',context)




# 3. 회원리스트
def mlist(request):
  id = request.session['session_id']
  if id == 'admin':
    qs = Member.objects.all()
  else:
    qs = Member.objects.filter(id=id)

  context = {"mlist":qs}
  return render(request,'mlist.html',context)





# 2. 로그아웃
def logout(request):
  request.session.clear() # 전체섹션삭제
  # del request.session['session_id'] # 해당섹션삭제
  return redirect("/") #url 로






# 1. 로그인 페이지, 로그인 버튼확인
def login(request):
  if request.method == "GET":
    return render(request,'login.html')
  else: # 로그인 버튼클릭
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      msg = "로그인이 되었습니다."
      print(msg)
      ## 섹션연결
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName

      return redirect('index') #app이름으로
    else:
      msg = "아이디 또는 패스워드가 일치하지 않습니다."
      print(msg)
      return render(request,"login.html",{"login_msg":msg})