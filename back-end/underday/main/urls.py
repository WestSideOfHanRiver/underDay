from django.urls import path
from . import views



urlpatterns = [
    # path('users/', views.user_list, name='user_list'),
    # path('classlist/', views.class_list, name='class_list'), # 메인페이지 수강리스트
    # path('getclassdate/', views.get_classdate, name='get_classdate'), # 회원관리 회원 정보 상세 요청
    # path('trmbship/', views.trmbship_list, name='trmbship_list'), # 멤버쉽 리스트
    # path('classrequest/', views.class_request, name='class_request'),
    # path('makeclass/', views.make_class, name='make_class'), # 강의 등록 수정 삭제
    # path('callmembers/', views.call_members, name='call_members'), # 회원 정보 요청
    # path('memberdetail/', views.member_detail, name='member_detail'), # 회원관리 회원 정보 상세 요청

    path('users/', views.UserListAPI.as_view(), name='user_list'),
    path("classlist/", views.ClassListAPI.as_view(), name="class_list"), # 메인페이지 수강리스트
    path('getclassdate/', views.GetClassdateAPI.as_view(), name='get_classdate'), # 회원관리 회원 정보 상세 요청
    path('trmbship/', views.TrmbshipListAPI.as_view(), name='trmbship_list'), # 멤버쉽 리스트
    path('classrequest/', views.ClassRequestAPI.as_view(), name='class_request'),
    path("makeclass/", views.MakeClassAPI.as_view(), name="make_class"), # 강의 등록 수정 삭제
    path('callmembers/', views.CallMembersAPI.as_view(), name='call_members'), # 회원 정보 요청
    path('memberdetail/', views.MembersDetailAPI.as_view(), name='member_detail'), # 회원관리 회원 정보 상세 요청

]
