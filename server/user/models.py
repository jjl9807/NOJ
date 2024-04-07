from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, null=False, primary_key=True)
    password = models.CharField(max_length=50, null=False)  # 密码 (MD5加密)
    nickname = models.CharField(max_length=50, null=False)  # 昵称
    reg_time = models.DateTimeField(auto_now=True)  # 注册时间
    qq = models.CharField(max_length=50, null=True, default="")
    email = models.CharField(max_length=50, null=True, default="")
    type = models.IntegerField(null=False, default=1)  # 1 普通 2 管理员

    objects = models.Manager()

    def __str__(self):
        return self.username


class UserStatus(models.Model):
    username = models.CharField(max_length=50, null=False, primary_key=True)
    ac = models.IntegerField(null=False, default=0)
    submit = models.IntegerField(null=False, default=0)
    score = models.IntegerField(default=0)
    des = models.CharField(max_length=50, null=True)
    rating = models.IntegerField(default=1500)
    acpro = models.TextField(null=True, default="")

    objects = models.Manager()

    def __str__(self):
        return self.username


class UserLoginRecord(models.Model):
    username = models.CharField(max_length=50, null=False)
    ip = models.CharField(max_length=50, null=True, default="unknow")
    login_time = models.DateTimeField(auto_now=True)
    msg = models.TextField(null=True)

    objects = models.Manager()

    def __str__(self):
        return self.username


class GlobalSettings(models.Model):
    """
    全局设置
    """

    oj_name = models.CharField(default="NOJ", max_length=100)
    language = models.CharField(
        max_length=500, default="C++|C|Python3|Python2|Swift5.1|Java")
    open_oi = models.BooleanField(default=True)
    open_code = models.BooleanField(default=True)  # 代码查看

    open_visitor = models.BooleanField(default=True)  # 游客访问
    open_register = models.BooleanField(default=True)  # 开放注册
    open_testcase = models.BooleanField(default=True)  # 测试用例

    objects = models.Manager()

    def __str__(self):
        return self.oj_name
