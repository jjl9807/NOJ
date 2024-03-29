from rest_framework.permissions import AllowAny
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .models import Problem, ProblemInfo, ProblemTag
from .serializers import ProblemSerializer, ProblemInfoSerializer, ProblemTagSerializer
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class ProblemView(viewsets.GenericViewSet, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    filter_fields = ('priv',)
    permission_classes = (AllowAny,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class ProblemInfoView(viewsets.ModelViewSet):

    queryset = ProblemInfo.objects.extra(
        select={'t': 'pid+0'}).extra(order_by=["-t"])
    serializer_class = ProblemInfoSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('priv')
    search_fields = ('tag', 'title')
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class ProblemTagView(viewsets.ModelViewSet):
    queryset = ProblemTag.objects.all()
    serializer_class = ProblemTagSerializer
    permission_classes = (AllowAny,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]
