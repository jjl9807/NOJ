from django.urls import path, re_path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('contestannouncement', views.ContestAnnouncementView)
routers.register('contestinfo', views.ContestInfoView)
routers.register('contestproblem', views.ContestProblemView)
routers.register('contestboard', views.ContestBoardView)
routers.register('contestplayer', views.ContestPlayerView)
routers.register('contesttotalboard', views.ContestBoardTotalView)

urlpatterns = [
    path('', include(routers.urls)),
    re_path(r'^currenttime', views.CurrentTimeView.as_view()),
    re_path(r'^contestfilterboard', views.ContestBoardFilterAPIView.as_view()),
    re_path(r'^isboardlock', views.ContestIsBoardLockAPIView.as_view()),

]
