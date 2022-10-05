from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('rooms', include('rooms.urls')),
    path('chat', include('chat.urls')),
    path('admin/', admin.site.urls),
]
