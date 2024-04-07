from django.db import models


class SubmissionResult(models.Model):

    user = models.CharField(max_length=50)
    problem = models.CharField(max_length=50)
    result = models.IntegerField()
    time = models.IntegerField()
    memory = models.IntegerField()
    length = models.IntegerField()  # 代码长度
    language = models.CharField(max_length=50)
    submit_time = models.DateTimeField()
    judger = models.CharField(max_length=50)  # 评测机
    contest = models.IntegerField()
    contest_problem = models.IntegerField(default=-1)  # 比赛内部题号
    code = models.TextField(max_length=200000)
    error_case = models.CharField(max_length=50, default="0")  # 错误测试点
    message = models.TextField()  # CE信息, RE信息等
    problem_title = models.CharField(max_length=100, default="")  # 题目标题
    ip = models.CharField(max_length=50, default="无法获取ip")

    objects = models.Manager()

    def __str__(self):
        return self.user


class CaseDetail(models.Model):

    submit_id = models.IntegerField()  # 提交ID
    username = models.CharField(max_length=50)
    problem = models.CharField(max_length=50)
    result = models.CharField(max_length=500, default="System Error")
    time = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    testcase = models.CharField(max_length=500, default="unknow")
    casedata = models.CharField(max_length=500)  # 是否显示测试数据
    outputdata = models.CharField(max_length=500, default="")
    useroutput = models.CharField(max_length=500, default="")

    objects = models.Manager()

    def __str__(self):
        return self.statusid
