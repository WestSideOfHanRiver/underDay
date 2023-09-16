
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('classlist/', views.class_list, name='class_list'), # 강의리스트
    path('trmbship/', views.trmbship_list, name='trmbship_list'), # 수강권 리스트
    path('classrequest/', views.class_request, name='class_request'), # CLASS CRUD
    path('peoplelist/', views.people_list, name='people_list'), # 강사회원리스트
    path('peoplemanage/', views.people_manage, name='people_manage'), # 강사회원관리

]
