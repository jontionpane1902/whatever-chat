from django.urls import path

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(
        {'post': 'create'}), name='chat_api'),
]
