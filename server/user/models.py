from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    ac = models.IntegerField(verbose_name="AC数", null=False, default=0)
    submit = models.IntegerField(verbose_name="提交数", null=False, default=0)
    desc = models.CharField(verbose_name="用户简介", max_length=50, null=True, default="")
    ac_pid = models.TextField(verbose_name="AC题号", null=True, default="")

    objects = UserManager()

    def __str__(self):
        return self.username


class GlobalSettings(models.Model):
    """
    全局设置
    """

    oj_name = models.CharField(
        verbose_name="OJ名称", default="NOJ", max_length=100)
    language = models.CharField(verbose_name="编程语言",
                                max_length=500, default="C++|C|Python3|Python2|Swift5.1|Java")
    open_oi = models.BooleanField(verbose_name="OI赛制", default=True)
    open_code = models.BooleanField(verbose_name="代码查看", default=True)

    open_visitor = models.BooleanField(verbose_name="游客访问", default=True)
    open_register = models.BooleanField(verbose_name="开放注册", default=True)
    open_testcase = models.BooleanField(verbose_name="显示用例", default=True)

    objects = models.Manager()

    def __str__(self):
        return self.oj_name
