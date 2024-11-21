
from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    #로그인관련
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #회원정보관련
    path('mlist/', views.mlist, name='mlist'), # 회원리스트
    path('mwrite/', views.mwrite, name='mwrite'), #회원입력
    path('mview/<str:id>/', views.mview, name='mview'), #회원상세
    path('mupdate/<str:id>/', views.mupdate, name='mupdate'), #회원수정
    path('mdelete/<str:id>/', views.mdelete, name='mdelete'), #회원삭제
]
