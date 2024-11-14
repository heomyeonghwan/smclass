from django.shortcuts import render

# Create your views here.
def eventview(request):
  return render(request,'eventview.html')