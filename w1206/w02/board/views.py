from django.shortcuts import render
from board.models import Board
from member.models import Member

# blist
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context ={"blist":qs}
  return render(request,"blist.html",context)


# bwrite
def bwrite(request):
  if request.method =="GET":
    return render(request,'bwrite.html')
  else:
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")

    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    
    qs.bgroup = qs.bno
    qs.save()

    context ={"wmsg":"1"}
    return render(request,'bwrite.html',context)