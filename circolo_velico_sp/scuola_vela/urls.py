from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sv_index, name='sv_index'),
    path('new/<str:ol>/', views.uscita_new, name='sv_uscita_new'),
    path('edit/<int:pk>/', views.uscita_edit, name='sv_uscita_edit'),
    path('delate/<int:pk>/', views.uscita_delete, name='sv_uscita_delete'),
    path('view/<int:pk>/', views.uscita_view, name='sv_uscita_view')
]
