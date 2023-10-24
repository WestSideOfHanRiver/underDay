from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('chkUserId/', views.chkUserId, name='chkUserId'),
    path('mypage/', views.mypage, name='mypage'),
]