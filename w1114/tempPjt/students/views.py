from django.shortcuts import render

# Create your views here.
def regStudents(request):
  return render(request,'register.html')