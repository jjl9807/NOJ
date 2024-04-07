from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('submission', views.SubmissionResultView)
routers.register('submit', views.SubmitView, basename='submit')
routers.register('code', views.SubmissionResultCodeView, basename='code')
routers.register('case', views.CaseDetailView)

urlpatterns = [
    path('', include(routers.urls)),
]
