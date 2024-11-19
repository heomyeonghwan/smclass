from django.shortcuts import render,redirect
from students.models import Student

#학생입력
def write(request):
  if request.method == "POST":
    name = request.POST.get('name') # 데이터가 없을때 None
    major = request.POST.get('major')
    grade = request.POST['grade']   # 데이터가 없을때 error
    age = request.POST['age']   
    gender = request.POST['gender'] 
    hobbys = request.POST.getlist('hobby')

    qs = Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
    qs.save()
    
    return redirect('/')
  else:
    return render(request,'write.html')


# 학생리스트
def list(request):
  return render(request,'list.html')