from django.db import models

# 

class Member(models.Model):
  id = models.CharField(primary_key=True,max_length=100)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nicName = models.CharField(max_length=100)
  phone = models.CharField(max_length=20,default="010-0000-0000")
  gender = models.CharField(max_length=10,default="남자")
  hobby = models.CharField(max_length=100,default="game")
  mdate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.id},{self.name},{self.nicName},{self.mdate}"