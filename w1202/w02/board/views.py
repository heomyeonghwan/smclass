from django.shortcuts import render
from board.models import Board
from member.models import Member


# 게시판리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context ={"blist":qs}
  return render(request,'blist.html',context)


# 게시글 상세보기
def bview(request,bno):
  qs = Board.objects.filter(bno=bno)
  context = {"board":qs[0]}
  print(qs)
  return render(request,'bview.html',context)

# 게시판 글쓰기
def bwrite(request):
  if request.method == "GET":
    return render(request,"bwrite.html")
  else:
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")

    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent)

    qs.bgroup=qs.bno # 번호 생성 후에 입력
    qs.save()

    context ={"wmsg":"1"}
    return render(request,'bwrite.html',context)