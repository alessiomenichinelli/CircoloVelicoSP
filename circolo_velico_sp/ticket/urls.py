from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/', views.ticket_list, name='ticket_list'),
    path('ticket/new/', views.ticket_new, name='ticket_new'),
    path('ticket/edit/<int:pk>', views.ticket_edit, name='ticket_edit'),
    path('ticket/delete/<int:pk>', views.ticket_delete, name='ticket_delete'),

]
