from django.shortcuts import render
from board.models import Board
from member.models import Member

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
