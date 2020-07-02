from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework import request
from api.models import User
from utils.response import APIResponse
from rest_framework import settings


class TestAPIView(APIView):
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