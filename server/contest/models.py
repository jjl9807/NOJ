from django.db import models


class ContestInfo(models.Model):
    """
    比赛信息表
    """

    organizer = models.CharField(
        verbose_name="组织人", max_length=50, default="admin")
    title = models.CharField(
        verbose_name="比赛标题", max_length=50, default="contest")
    level = models.IntegerField(verbose_name="比赛难度", default=1)
    des = models.CharField(verbose_name="比赛简介",
                           max_length=500, default="contest des")
    note = models.CharField(
        verbose_name="比赛提示", max_length=500, default="contest note")
    begintime = models.DateTimeField(verbose_name="开始时间", )
    lasttime = models.IntegerField(verbose_name="持续时间", default=18000)
    type = models.CharField(verbose_name="比赛赛制", max_length=50, default="ACM")
    priv = models.IntegerField(
        verbose_name="比赛权限", default=2)  # 1 public 2 private
    iprange = models.CharField(
        verbose_name="IP限制", max_length=2000, default="iprange")

    lockboard = models.IntegerField(verbose_name="是否封榜", default=0)  # 0 不封 1 封
    locktime = models.IntegerField(verbose_name="封榜时间", default=0)  # 最后多少分钟封榜

    objects = models.Manager()

    def __str__(self):
        return self.creator


class ContestAnnouncement(models.Model):
    """
    比赛公告表
    """

    contestid = models.IntegerField(verbose_name="公告ID", )
    announcement = models.CharField(verbose_name="公告内容", max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestProblem(models.Model):
    """
    比赛题目表
    """

    contestid = models.IntegerField(verbose_name="比赛ID", )
    problemid = models.CharField(verbose_name="题目ID", max_length=50)
    problemtitle = models.CharField(
        verbose_name="题目标题", max_length=500, default="uname")
    rank = models.IntegerField(verbose_name="题目序号", )  # 顺序

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestBoard(models.Model):
    """
    比赛排行榜
    """

    contestid = models.IntegerField(verbose_name="比赛ID", )
    username = models.CharField(verbose_name="用户名", max_length=50)
    user = models.CharField(verbose_name="用户昵称", max_length=50)
    problemrank = models.IntegerField(verbose_name="题目（比赛内）序号", )
    # type: 1 AC， 0 没AC算罚时，-1 没AC不算罚时, 2 封榜中，不算罚时(只会在后端做修改)
    type = models.IntegerField(verbose_name="提交结果", )
    submittime = models.BigIntegerField(verbose_name="提交时间", )  # 毫秒单位
    submitid = models.IntegerField(verbose_name="提交ID", )

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestPlayer(models.Model):
    """
    比赛选手
    """

    contestid = models.IntegerField(verbose_name="比赛ID", )
    user = models.CharField(verbose_name="用户名", max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestBoardTotal(models.Model):

    user = models.CharField(verbose_name="用户名", max_length=100)
    nickname = models.CharField(verbose_name="用户昵称", max_length=100)
    contestid = models.IntegerField(verbose_name="比赛ID", )
    score = models.IntegerField(verbose_name="得分", )
    time = models.CharField(verbose_name="比赛耗时", max_length=100)
    detail = models.CharField(verbose_name="详情", max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.user
