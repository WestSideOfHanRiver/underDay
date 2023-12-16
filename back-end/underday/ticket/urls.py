from django.urls import path
from . import views

urlpatterns = [
    # 티켓
    path("ticket_list/", views.TicketListAPI.as_view(), name="ticket_list"),
    path("create/", views.TicketCreateAPI.as_view(), name="create"),
    path("update/", views.TicketUpdateAPI.as_view(), name="update"),
    path("trMbshipList/", views.trMbshipListAPI.as_view(), name="trMbshipList"),
]
