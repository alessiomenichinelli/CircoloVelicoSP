from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.b_index, name='b_index'),
    path('new/<str:tm>/', views.uscita_new, name='b_uscita_new'),
    path('edit/<int:pk>/', views.uscita_edit, name='b_uscita_edit'),
    path('delate/<int:pk>/', views.uscita_delete, name='b_uscita_delete'),
    path('view/<int:pk>/', views.uscita_view, name='b_uscita_view'),
]
