from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from .models import SubmissionResult, CaseDetail
from .serializers import SubmissionResultSerializer, SubmissionCodeSerializer, CaseDetailSerializer
# from .permission import ManagerOnly, UserRatingOnly, NoContestOnly
# from contest.models import ContestInfo
# from contest.serializers import ContestInfoSerializer
import datetime


class SubmissionResultView(viewsets.ModelViewSet):
    queryset = SubmissionResult.objects.all().order_by('-id')
    serializer_class = SubmissionResultSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'result', "contest",
                     "problem", "language", "problemtitle")
    # permission_classes = (ManagerOnly,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def list(self, request, *args, **kwargs):
        # self.check_permissions(request)
        self.check_throttles(request)

        user_id = request._request.session.get("user_id")
        user_type = request._request.session.get("type")

        cid = request._request.GET.get("contest", 0)
        if cid == "":
            cid = 0
        contest_id = int(cid)

        if contest_id == 0:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        # else:  # 封榜特判
        #     contest = ContestInfo.objects.get(id=contestid)

        #     queryset = self.filter_queryset(self.get_queryset())
        #     newpage = []
        #     for data in queryset:
        #         if usertype != 3 and userid != data.user and contest.lockboard == 1 and contest.lasttime - (data.submittime - contest.begintime).total_seconds() <= contest.locktime * 60:
        #             data.result = -1
        #         newpage.append(data)
        #     page = self.paginate_queryset(newpage)
        #     if page is not None:
        #         serializer = self.get_serializer(page, many=True)
        #         return self.get_paginated_response(serializer.data)
        #     serializer = self.get_serializer(newpage, many=True)
        #     return Response(serializer.data)


class SubmitView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    # 提交接口
    queryset = SubmissionResult.objects.all()
    serializer_class = SubmissionCodeSerializer
    # permission_classes = (UserRatingOnly,)
    throttle_scope = "judge"
    throttle_classes = [ScopedRateThrottle, ]


class SubmissionResultCodeView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = SubmissionResult.objects.all()
    serializer_class = SubmissionCodeSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'result', "contest", "problem", "problemtitle")
    # permission_classes = (NoContestOnly,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class CaseDetailView(viewsets.ModelViewSet):
    queryset = CaseDetail.objects.all()
    serializer_class = CaseDetailSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username', 'problem', "statusid")
    # permission_classes = (ManagerOnly,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]
