from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('sv/', include('scuola_vela.urls')),
    path('barche/', include('barche.urls')),
    path('', include('ticket.urls')),
]
