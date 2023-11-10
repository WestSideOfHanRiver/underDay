from django.urls import path
from . import views

urlpatterns = [
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('trMbshipList/', views.trMbshipList, name='trMbshipList'),
]
