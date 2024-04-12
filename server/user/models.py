from django.db import models


class User(models.Model):
    username = models.CharField(
        verbose_name="用户名", max_length=50, null=False, primary_key=True)
    password = models.CharField(
        verbose_name="密码", max_length=50, null=False)  # MD5
    nickname = models.CharField(verbose_name="昵称", max_length=50, null=False)
    reg_time = models.DateTimeField(verbose_name="注册时间", auto_now=True)
    qq = models.CharField(
        verbose_name="QQ", max_length=50, null=True, default="")
    email = models.CharField(
        verbose_name="邮箱", max_length=50, null=True, default="")
    type = models.IntegerField(
        verbose_name="用户类型", null=False, default=1)  # 1 普通 2 管理员

    objects = models.Manager()

    def __str__(self):
        return self.username


class UserStatus(models.Model):
    username = models.CharField(
        verbose_name="用户名", max_length=50, null=False, primary_key=True)
    ac = models.IntegerField(verbose_name="AC数", null=False, default=0)
    submit = models.IntegerField(verbose_name="提交数", null=False, default=0)
    des = models.CharField(verbose_name="用户简介", max_length=50, null=True)
    acpro = models.TextField(verbose_name="AC题号", null=True, default="")

    objects = models.Manager()

    def __str__(self):
        return self.username


class UserLoginRecord(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=50, null=False)
    ip = models.CharField(verbose_name="登陆IP",
                          max_length=50, null=True, default="unknow")
    login_time = models.DateTimeField(verbose_name="登陆时间", auto_now=True)
    msg = models.TextField(verbose_name="其他信息", null=True)

    objects = models.Manager()

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
