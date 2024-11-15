from django.shortcuts import render

# Create your views here.
def write(request):
  return render(request,'write.html')

def save(request):
  print("학생정보저장 호출")