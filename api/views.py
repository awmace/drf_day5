from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework import request

from api.authentications import MyAuth
from api.models import User
from api.throttle import SendMessageRate
from utils.response import APIResponse
from rest_framework import settings
from rest_framework.authentication import BasicAuthentication


class TestAPIView(APIView):
    # 局部自定义认证器
    authentication_classes = [MyAuth]
    def get(self, request, *args, **kwargs):
        # # 查询用户
        # user = User.objects.first()
        # # 根据用户获取对应的角色
        # print(user.groups.first())
        # # 根据用户获取用户对应的权限
        # print(user.user_permissions.first().name)

        # 获取角色
        # group = Group.objects.first()
        # print(group)
        # # 通过角色获取对应的权限
        # print(group.permissions.first().name)
        # # 根据角色获取对应的用户
        # print(group.user_set.first().username)

        # 获取权限
        per = Permission.objects.filter(pk=9).first()
        print(per.name)
        # 根据权限获取用户
        print(per.user_set.first().username)
        # 根据权限获取角色
        per = Permission.objects.filter(pk=13).first()
        print(per.group_set.first().name)

        return APIResponse('ok')


class TestPermissionAPIView(APIView):
    # 只有认证后的才可以访问

    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse("登录访问成功")


class UserLoginOrReadOnly(APIView):

    # 用户登录可写  游客浏览只读

    throttle_classes = [UserRateThrottle]

    # permission_classes = [MyPermission]

    def get(self, request, *args, **kwargs):
        return APIResponse("read成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("write写操作")


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse("read成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("write写操作")