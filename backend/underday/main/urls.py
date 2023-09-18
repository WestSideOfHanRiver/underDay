from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('classlist/', views.class_list, name='class_list'),
    path('trmbship/', views.trmbship_list, name='trmbship_list'),
    path('classrequest/', views.class_request, name='class_request'),

]
