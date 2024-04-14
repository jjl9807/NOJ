from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import ScopedRateThrottle
from .models import User, GlobalSettings
from .serializers import UserBasicSerializer, UserLoginSerializer, UserRegisterSerializer, UserSerializer, UserStatusSerializer, UserNoPassSerializer, UserNoTypeSerializer, GlobalSettingsSerializer
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate, login, logout
# from .permission import UserSafePostOnly, UserPUTOnly, AuthPUTOnly, ManagerOnly


class GlobalSettingsView(viewsets.ModelViewSet):
    queryset = GlobalSettings.objects.all()
    serializer_class = GlobalSettingsSerializer
    # permission_classes = (ManagerOnly,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


def getRegisterPermission(request):
    setting = GlobalSettings.objects.filter(id=1)
    if len(setting) != 0:
        if setting[0].open_register is False:
            return False
        else:
            return True
    else:
        return True


class UserStatusView(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-ac')  # 根据AC数量降序排列
    serializer_class = UserStatusSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)
    # permission_classes = (UserSafePostOnly,)
    pagination_class = LimitOffsetPagination
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserNoPassSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('username',)
    search_fields = ('username', 'nickname', 'email', 'qq')
    # permission_classes = (UserSafePostOnly,)
    pagination_class = LimitOffsetPagination
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]


class UserChangeView(APIView):

    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def put(self, request, format=None):
        data = request.data.copy()
        username = request.session.get('user_id', None)
        if username != None:
            user = User.objects.get(username=username)
            user.password = data["password"]
            user.nickname = data["nickname"]
            user.email = data["email"]
            user.desc = data["des"]
            user.save()

            return Response("ok", status=HTTP_200_OK)

        return Response("nologin", status=HTTP_400_BAD_REQUEST)


class UserChangeAllView(APIView):
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    def put(self, request, format=None):
        if request.session.get('type', None) != 3:
            return Response("no permission", status=HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        username = data["username"]
        if username != None:
            user = User.objects.get(username=username)
            if data["password"] != ".":
                user.password = data["password"]
            user.nickname = data["nickname"]
            user.email = data["email"]
            user.save()
            return Response("ok", status=HTTP_200_OK)
        return Response("username error", status=HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    """
    用户登录
    """
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    @swagger_auto_schema(request_body=UserLoginSerializer, responses={200: UserBasicSerializer, 400: "Invalid login."})
    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        print(username)
        password = data.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserBasicSerializer(user)
            return Response(serializer.data, HTTP_200_OK)
        else:
            return Response("Invalid login.", HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    """
    用户登出
    """
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    @swagger_auto_schema(responses={200: "You're logged out."})
    def get(self, request):
        logout(request)
        # return HttpResponseRedirect('/')
        return Response("You're logged out.", HTTP_200_OK)


class UserRegisterAPIView(APIView):
    """
    用户注册
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    throttle_scope = "post"
    throttle_classes = [ScopedRateThrottle, ]

    @swagger_auto_schema(request_body=UserRegisterSerializer, responses={200: UserBasicSerializer(), 400: "Duplicate username!"})
    def post(self, request, format=None):
        if getRegisterPermission(request) == False:
            return Response("Register is not open!", status=HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        username = data.get('username')
        if User.objects.filter(username__exact=username):
            return Response("Duplicate username!", HTTP_400_BAD_REQUEST)
        password = data.get('password')
        email = data.get('email')
        user = User.objects.create_user(
            username=username, password=password, email=email)
        if user:
            serializer = UserBasicSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response("System error!", status=HTTP_400_BAD_REQUEST)
