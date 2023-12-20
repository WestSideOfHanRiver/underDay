from django.urls import path
from . import views

urlpatterns = [
    # 수업권한권
    path("classManagement/", views.ClassManagementAPI.as_view(), name="classManagement"),
    path("sportsList/", views.SportsListAPI.as_view(), name="sportsList"),
]