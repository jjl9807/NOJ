from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('problem', views.ProblemView)
routers.register('pstatus', views.ProblemMetaView)
routers.register('ptag', views.ProblemTagView)

urlpatterns = [
    path('', include(routers.urls)),
    # path(r'^uploadfile', views.UploadFileAPIView.as_view()),
    # path(r'^downloadfile/', views.filedown, name='download'),
    # path(r'^showpic/', views.showpic, name='show_picture'),
    # path(r'^judgerdownloadfile/', views.judgerfiledown, name='judgerfiledown'),
    # path(r'^judgerfiletime/', views.judgerfiletime, name='judgerfiletime'),
]
