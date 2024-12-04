from django.shortcuts import render
from board.models import Board
from member.models import Member
from django.db.models import F
from django.db.models import Q
from django.core.paginator import Paginator




# # 게시판리스트 
# def blist(request):
#   # order_by : 정렬, - : 역순정렬
#   qs = Board.objects.all().order_by("-bgroup","bstep")

#   context ={"blist":qs}
#   return render(request,'blist.html',context)




# 게시글 상세보기
def bview(request,bno):
  nowpage = request.GET.get("page",1)
  qs = Board.objects.get(bno=bno) # 현재글
  qs.bhit = qs.bhit + 1
  qs.save()

  next_qs = Board.objects.filter(Q(bgroup__gt=qs.bgroup,bstep__gte=qs.bstep)|Q(bgroup=qs.bgroup,bstep__lt=qs.bstep)).order_by("-bgroup","bstep").last()
  prev_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)|Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by("-bgroup","bstep").first()

  print("이전글: ",prev_qs.bno)
  context = {"board":qs,"nowpage":nowpage,"next_board":next_qs,"prev_board":prev_qs}
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
    nowpage= request.GET.get("page",1)

    qs = Board.objects.get(bno=bno)
    context ={"board":qs,"nowpage":nowpage}
    return render(request,"bupdate.html",context)
  else:
    nowpage= request.POST.get("page",1)

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
    context = {"umsg":"1","nowpage":nowpage}
    return render(request,"bupdate.html",context)
  


# 답글달기
def breply(request,bno):
  if request.method == "GET":
    nowpage = request.GET.get("page",1)
    
    qs =Board.objects.get(bno=bno)
    context = {"board":qs,"nowpage":nowpage}
    return render(request,"breply.html",context)
  else:
    nowpage = request.POST.get("page",1)

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
    
    context ={"rmsg":"1","nowpage":nowpage}
    return render(request,'breply.html',context)



# 게시판리스트 / 페이지처리
def blist(request):
  # order_by : 정렬, - : 역순정렬
  qs = Board.objects.all().order_by("-bgroup","bstep")
  paginator = Paginator(qs,10) # 100개 > 10개씩 분리작업
  nowpage = int(request.GET.get("page",1)) # 현재 몇페이지를 요청했는지 확인
  list_qs = paginator.get_page(nowpage) # 요청된 페이지의 번호를 가져옴
  context ={"blist":list_qs,"nowpage":nowpage}
  return render(request,'blist.html',context)