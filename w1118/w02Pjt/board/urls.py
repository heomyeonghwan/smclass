from django.urls import path,include
from . import views

app_name='list'
urlpatterns = [
    path('list/', views.list,name='list'),
]
