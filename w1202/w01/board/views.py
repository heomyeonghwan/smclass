from django.shortcuts import render
from board.models import Board
from member.models import Member
from django.db.models import F


# 게시판리스트 
def blist(request):
  # order_by : 정렬, - : 역순정렬
  qs = Board.objects.all().order_by("-bgroup","bstep")

  context ={"blist":qs}
  return render(request,'blist.html',context)



# 게시글 상세보기
def bview(request,bno):
  qs = Board.objects.get(bno=bno)
  qs.bhit = qs.bhit + 1
  qs.save()
  context = {"board":qs}
  return render(request,"bview.html",context)


# 게시판 글쓰기
def bwrite(request):
  if request.method =="GET":
    return render(request,"bwrite.html")
  else:
    # post방식
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")

    # board 저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)

    # bgroup은 이후입력
    qs.bgroup = qs.bno
    qs.save()

    context ={"wmsg":"1"}
    return render(request,"bwrite.html",context)


# 게시글 삭제
def bdelete(request,bno):
  qs =Board.objects.get(bno=bno)
  qs.delete()

  context ={"dmsg":bno}

  return render(request,'blist.html',context)


# 게시글 수정
def bupdate(request,bno):
  if request.method=="GET":
    qs = Board.objects.get(bno=bno)
    context ={"board":qs}
    return render(request,"bupdate.html",context)
  else:
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")

    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    if bfile:
      qs.bfile = bfile
    qs.save()
    context = {"umsg":"1"}
    return render(request,"bupdate.html",context)
  


# 답글달기
def breply(request,bno):
  if request.method == "GET":
    qs =Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,"breply.html",context)
  else:
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    bgroup = request.POST.get("bgroup")
    bstep = int(request.POST.get("bstep")) # 문자 > int타입변경
    bindent = int(request.POST.get("bindent")) # 문자 > int타입변경

    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile")

    # 검색 2가지
    # Board.objects.get(bno=bno) 리턴1개
    # qs.save()
    # Board.objects.filter(bno=bno) 리턴 여러개
    # update()


    # 부모보다 큰 bstep은 1증가
    # 기존에 있는 답글들 1증가
    qs = Board.objects.filter(bgroup = bgroup, bstep__gt = bstep) # bstep > bstep
    qs.update(bstep = F("bstep")+1)

    # 새로 입력받은 답글 1증가
    Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile)
    
    context ={"rmsg":"1"}
    return render(request,"breply.html",context)