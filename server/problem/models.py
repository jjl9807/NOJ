from django.db import models

# Create your models here.


class Problem(models.Model):
    pid = models.CharField(max_length=50, primary_key=True)
    author = models.CharField(max_length=50, default="admin")
    time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=500)
    desc = models.TextField()
    in_desc = models.TextField()
    out_desc = models.TextField()
    in_sample = models.TextField()
    out_sample = models.TextField()
    time_limit = models.IntegerField()
    mem_limit = models.IntegerField()
    hint = models.TextField(null=True, default="")
    priv = models.IntegerField(default=1)  # 题目权限：1 公开 2 私密 3 仅限比赛
    type = models.IntegerField(default=1)  # 题目类型：1 文本比较 2 样例池 3 动态样例

    objects = models.Manager()

    def __str__(self):
        return self.title


class ProblemInfo(models.Model):
    pid = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=500)
    level = models.IntegerField(default=1)  # 题目难度：1 简单 2 中等 3 困难
    submission = models.IntegerField(default=0)
    ac = models.IntegerField(default=0)
    mle = models.IntegerField(default=0)
    tle = models.IntegerField(default=0)
    rte = models.IntegerField(default=0)
    pe = models.IntegerField(default=0)
    ce = models.IntegerField(default=0)
    wa = models.IntegerField(default=0)
    se = models.IntegerField(default=0)
    tag = models.TextField(null=True)
    score = models.IntegerField(default=100)
    priv = models.IntegerField(default=1)  # 题目权限：1 公开 2 私密 3 仅限比赛

    objects = models.Manager()

    def __str__(self):
        return self.title


class ProblemTag(models.Model):
    tagname = models.CharField(max_length=50, unique=True)
    num = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.tagname
