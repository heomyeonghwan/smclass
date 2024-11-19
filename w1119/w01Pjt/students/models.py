from django.db import models

# 객체생성
class Student(models.Model):
  ## primary key 가 없으면 자동으로 pk=id가 생성
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=1)
  age = models.IntegerField(default=1)
  gender = models.CharField(max_length=10)
  hobby = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.name},{self.major},{self.grade}" # 문자열이되어야함