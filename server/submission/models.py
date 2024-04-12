from django.db import models


class SubmissionResult(models.Model):

    user = models.CharField(verbose_name="提交用户", max_length=50)
    problem = models.CharField(verbose_name="题目", max_length=50)
    result = models.IntegerField(verbose_name="结果", )
    time = models.IntegerField(verbose_name="用时", )
    memory = models.IntegerField(verbose_name="内存", )
    length = models.IntegerField(verbose_name="代码长度", )
    language = models.CharField(verbose_name="编程语言", max_length=50)
    submit_time = models.DateTimeField(verbose_name="提交时间", )
    contest = models.IntegerField(verbose_name="所属比赛", )
    contest_problem = models.IntegerField(
        verbose_name="比赛内部题号", default=-1)
    code = models.TextField(verbose_name="代码", max_length=200000)
    error_case = models.CharField(
        verbose_name="错误用例", max_length=50, default="0")
    message = models.TextField(verbose_name="其他错误消息", )
    problem_title = models.CharField(
        verbose_name="题目标题", max_length=100, default="")
    ip = models.CharField(verbose_name="提交IP", max_length=50, default="无法获取ip")

    objects = models.Manager()

    def __str__(self):
        return self.user


class CaseDetail(models.Model):

    submit_id = models.IntegerField(verbose_name="提交ID", )  # 提交ID
    username = models.CharField(verbose_name="用户名", max_length=50)
    problem = models.CharField(verbose_name="题目", max_length=50)
    result = models.CharField(
        verbose_name="结果", max_length=500, default="System Error")
    time = models.IntegerField(verbose_name="用时", default=0)
    memory = models.IntegerField(verbose_name="内存", default=0)
    testcase = models.CharField(
        verbose_name="测试用例名称", max_length=500, default="unknow")
    casedata = models.CharField(
        verbose_name="测试用例数据", max_length=500)  # 注意是否显示测试数据
    outputdata = models.CharField(
        verbose_name="正确输出", max_length=500, default="")
    useroutput = models.CharField(
        verbose_name="用户输出", max_length=500, default="")

    objects = models.Manager()

    def __str__(self):
        return self.statusid
