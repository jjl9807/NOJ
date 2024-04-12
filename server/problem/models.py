from django.db import models

# Create your models here.


class Problem(models.Model):
    pid = models.CharField(verbose_name="题目ID",
                           max_length=50, primary_key=True)
    author = models.CharField(
        verbose_name="出题人", max_length=50, default="admin")
    time = models.DateTimeField(verbose_name="发布时间", auto_now=True)
    title = models.CharField(verbose_name="题目标题", max_length=500)
    desc = models.TextField(verbose_name="题目描述", )
    in_desc = models.TextField(verbose_name="输入描述", )
    out_desc = models.TextField(verbose_name="输出描述", )
    in_sample = models.TextField(verbose_name="输入样例", )
    out_sample = models.TextField(verbose_name="输出样例", )
    time_limit = models.IntegerField(verbose_name="时间限制", )
    mem_limit = models.IntegerField(verbose_name="内存限制", )
    hint = models.TextField(verbose_name="提示", null=True, default="")
    priv = models.IntegerField(
        verbose_name="题目权限", default=1)  # 1 公开 2 私密 3 仅限比赛
    type = models.IntegerField(
        verbose_name="题目类型", default=1)  # 1 文本比较 2 样例池 3 动态样例

    objects = models.Manager()

    def __str__(self):
        return self.title


class ProblemInfo(models.Model):
    pid = models.CharField(verbose_name="题目ID",
                           max_length=50, primary_key=True)
    title = models.CharField(verbose_name="题目标题", max_length=500)
    level = models.IntegerField(
        verbose_name="题目难度", default=1)  # 1 简单 2 中等 3 困难
    submission = models.IntegerField(verbose_name="提交数量", default=0)
    ac = models.IntegerField(verbose_name="AC数量", default=0)
    mle = models.IntegerField(verbose_name="MLE数量", default=0)
    tle = models.IntegerField(verbose_name="TLE数量", default=0)
    rte = models.IntegerField(verbose_name="RTE数量", default=0)
    pe = models.IntegerField(verbose_name="PE数量", default=0)
    ce = models.IntegerField(verbose_name="CE数量", default=0)
    wa = models.IntegerField(verbose_name="WA数量", default=0)
    se = models.IntegerField(verbose_name="SE数量", default=0)
    tag = models.TextField(verbose_name="题目标签", null=True)
    score = models.IntegerField(verbose_name="题目分数", default=100)
    priv = models.IntegerField(
        verbose_name="题目权限", default=1)  # 1 公开 2 私密 3 仅限比赛

    objects = models.Manager()

    def __str__(self):
        return self.title


class ProblemTag(models.Model):
    tagname = models.CharField(verbose_name="标签内容", max_length=50, unique=True)
    num = models.IntegerField(verbose_name="使用数量", )

    objects = models.Manager()

    def __str__(self):
        return self.tagname
