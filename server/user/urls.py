from django.urls import path, re_path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('userstatus', views.UserStatusView)
routers.register('user', views.UserView)

urlpatterns = [
    path('', include(routers.urls)),
    re_path(r'^register', views.UserRegisterAPIView.as_view()),
    re_path(r'^login', views.UserLoginAPIView.as_view()),
    re_path(r'^logout', views.UserLogoutAPIView.as_view()),
    re_path(r'^changeone', views.UserChangeView.as_view()),
    re_path(r'^changeall', views.UserChangeAllView.as_view()),
]
