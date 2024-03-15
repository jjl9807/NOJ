from django.urls import path
from .views import PongView

urlpatterns = [
    path('ping', PongView.as_view(), name='ping-api'),
]