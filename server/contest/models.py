from django.db import models


class ContestInfo(models.Model):
    """
    比赛信息表
    """

    organizer = models.CharField(max_length=50, default="admin")
    oj = models.CharField(max_length=50, default="LPOJ")
    title = models.CharField(max_length=50, default="contest")
    level = models.IntegerField(default=1)
    des = models.CharField(max_length=500, default="contest des")
    note = models.CharField(max_length=500, default="contest note")
    begintime = models.DateTimeField()
    lasttime = models.IntegerField(default=18000)
    type = models.CharField(max_length=50, default="ACM")
    priv = models.IntegerField(default=2)  # 1 public 2 private
    iprange = models.CharField(max_length=2000, default="iprange")

    lockboard = models.IntegerField(default=0)  # 0 不封 1 封
    locktime = models.IntegerField(default=0)  # 最后多少分钟封榜

    objects = models.Manager()

    def __str__(self):
        return self.creator


class ContestAnnouncement(models.Model):
    """
    比赛公告表
    """

    contestid = models.IntegerField()
    announcement = models.CharField(max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestProblem(models.Model):
    """
    比赛题目表
    """

    contestid = models.IntegerField()
    problemid = models.CharField(max_length=50)
    problemtitle = models.CharField(max_length=500, default="uname")
    rank = models.IntegerField()  # 顺序

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestBoard(models.Model):
    """
    比赛排行榜
    """

    contestid = models.IntegerField()
    username = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    problemrank = models.IntegerField()
    type = models.IntegerField()  # 1 AC， 0没AC算罚时，-1没AC不算罚时, 2 封榜中，不算罚时(只会在后端做修改)
    submittime = models.BigIntegerField()  # 豪秒为单位
    submitid = models.IntegerField()  # 用于rejudge
    rating = models.IntegerField(default=1500)

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestPlayer(models.Model):
    """
    比赛选手
    """

    contestid = models.IntegerField()
    user = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.contestid


class ContestBoardTotal(models.Model):

    user = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    contestid = models.IntegerField()
    score = models.IntegerField()
    time = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.user
