from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
# from .permission import ManagerOnly, UserRatingOnly, UserRatingOnly2, UserOnly, UserOnly1
from .models import ContestAnnouncement, ContestBoard, ContestInfo, ContestProblem, ContestPlayer, ContestBoardTotal
from .serializers import ContestBoardTotalSerializer, ContestAnnouncementSerializer, ContestBoardSerializer, ContestInfoSerializer, ContestProblemSerializer, ContestPlayerSerializer
import datetime
# from user.models import User


class ContestAnnouncementView(viewsets.ModelViewSet):
    queryset = ContestAnnouncement.objects.all()
    serializer_class = ContestAnnouncementSerializer
    pagination_class = LimitOffsetPagination
    # permission_classes = (ManagerOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("contestid",)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class ContestBoardView(viewsets.ModelViewSet):
    queryset = ContestBoard.objects.all()
    serializer_class = ContestBoardSerializer
    # permission_classes = (UserRatingOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("contestid", "username", "problemrank", "type",)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class ContestInfoView(viewsets.ModelViewSet):
    queryset = ContestInfo.objects.all().order_by('-id')
    serializer_class = ContestInfoSerializer
    pagination_class = LimitOffsetPagination
    # permission_classes = (ManagerOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ("begintime", "level", "type", "title", "classes")
    search_fields = ('title',)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class ContestProblemView(viewsets.ModelViewSet):
    queryset = ContestProblem.objects.all().order_by('rank')
    serializer_class = ContestProblemSerializer
    pagination_class = LimitOffsetPagination
    # permission_classes = (ManagerOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('contestid',)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class ContestPlayerView(viewsets.ModelViewSet):
    queryset = ContestPlayer.objects.all()
    serializer_class = ContestPlayerSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (UserRatingOnly2,)
    filter_fields = ('user', "contestid")
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class CurrentTimeView(APIView):
    def get(self, request):
        return Response(datetime.datetime.now(), HTTP_200_OK)


class ContestBoardTotalView(viewsets.ModelViewSet):
    queryset = ContestBoardTotal.objects.all()
    serializer_class = ContestBoardTotalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (ManagerOnly,)
    filter_fields = ('user', 'nickname', "contestid")
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class ContestBoardFilterAPIView(APIView):

    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def post(self, request, format=None):
        # if request.session.get("type") != 3:
        #     return Response("nopermission", status=HTTP_400_BAD_REQUEST)

        data = request.data

        contestid = data.get("contestid")
        schoolname = data.get("school", "")
        coursename = data.get("course", "")
        classname = data.get("class", "")
        reslist = []
        boards = ContestBoard.objects.filter(contestid=contestid)
        contest = ContestInfo.objects.get(id=contestid)
        userid = request.session.get("user_id")
        usertype = request.session.get("type")

        usermap = {}

        for b in boards:
            # 封榜判断

            if usertype != 3 and userid != b.username and contest.lockboard == 1 and contest.lasttime - (datetime.datetime.fromtimestamp(b.submittime / 1000) - contest.begintime).total_seconds() <= contest.locktime * 60:
                b.type = 2

            username = b.username
            if usermap.get(username, None) != None:
                if usermap.get(username) == True:
                    reslist.append(b)
                continue

            user = User.objects.get(username=username)
            flag = True

            if schoolname != "":
                if str(user.school) != str(schoolname):
                    flag = False

            if coursename != "":
                if str(user.course) != str(coursename):
                    flag = False

            if classname != "":
                if str(user.classes) != str(classname):
                    flag = False

            if flag == True:
                reslist.append(b)

            usermap[username] = flag

       # res = ContestBoard.objects.filter(pk__in=reslist)
        return Response(ContestBoardSerializer(reslist, many=True).data, HTTP_200_OK)


class ContestIsBoardLockAPIView(APIView):

    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def post(self, request, format=None):

        data = request.data

        contestid = data.get("contestid")

        contest = ContestInfo.objects.get(id=contestid)

        if contest.lockboard == 1 and contest.lasttime - (datetime.datetime.now() - contest.begintime).total_seconds() <= contest.locktime * 60:
            return Response("yes", HTTP_200_OK)
        return Response("no", HTTP_200_OK)
