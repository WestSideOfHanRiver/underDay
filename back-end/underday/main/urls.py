from django.urls import path
from . import views



urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('classlist/', views.class_list, name='class_list'), # 메일페이지 수강리스트
    path('trmbship/', views.trmbship_list, name='trmbship_list'), # 멤버쉽 리스트
    path('classrequest/', views.class_request, name='class_request'),
    path('makeclass/', views.make_class, name='make_class'), # 강의 등록 수정 삭제
    path('callmembers/', views.call_members, name='call_members'), # 회원 정보 요청
    path('memberdetail/', views.member_detail, name='member_detail'), # 회원관리 회원 정보 상세 요청

]
