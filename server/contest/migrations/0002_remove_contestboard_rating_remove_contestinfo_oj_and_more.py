# Generated by Django 4.2.11 on 2024-04-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestboard',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='contestinfo',
            name='oj',
        ),
        migrations.RemoveField(
            model_name='contestplayer',
            name='rating',
        ),
        migrations.AlterField(
            model_name='contestannouncement',
            name='announcement',
            field=models.CharField(max_length=500, verbose_name='公告内容'),
        ),
        migrations.AlterField(
            model_name='contestannouncement',
            name='contestid',
            field=models.IntegerField(verbose_name='公告ID'),
        ),
        migrations.AlterField(
            model_name='contestboard',
            name='contestid',
            field=models.IntegerField(verbose_name='比赛ID'),
        ),
        migrations.AlterField(
            model_name='contestboard',
            name='problemrank',
            field=models.IntegerField(verbose_name='题目（比赛内）序号'),
        ),
        migrations.AlterField(
            model_name='contestboard',
            name='submitid',
            field=models.IntegerField(verbose_name='提交ID'),
        ),
        migrations.AlterField(
            model_name='contestboard',
            name='submittime',
            field=models.BigIntegerField(verbose_name='提交时间'),
        ),
        migrations.AlterField(
            model_name='contestboard',
            name='type',
            field=models.IntegerField(verbose_name='提交结果'),
        ),
        migrations.AlterField(
            model_name='contestboard',
            name='user',
            field=models.CharField(max_length=50, verbose_name='用户昵称'),
        ),
        migrations.AlterField(
            model_name='contestboard',
            name='username',
            field=models.CharField(max_length=50, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='contestboardtotal',
            name='contestid',
            field=models.IntegerField(verbose_name='比赛ID'),
        ),
        migrations.AlterField(
            model_name='contestboardtotal',
            name='detail',
            field=models.CharField(max_length=500, verbose_name='详情'),
        ),
        migrations.AlterField(
            model_name='contestboardtotal',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name='用户昵称'),
        ),
        migrations.AlterField(
            model_name='contestboardtotal',
            name='score',
            field=models.IntegerField(verbose_name='得分'),
        ),
        migrations.AlterField(
            model_name='contestboardtotal',
            name='time',
            field=models.CharField(max_length=100, verbose_name='比赛耗时'),
        ),
        migrations.AlterField(
            model_name='contestboardtotal',
            name='user',
            field=models.CharField(max_length=100, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='begintime',
            field=models.DateTimeField(verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='des',
            field=models.CharField(default='contest des', max_length=500, verbose_name='比赛简介'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='iprange',
            field=models.CharField(default='iprange', max_length=2000, verbose_name='IP限制'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='lasttime',
            field=models.IntegerField(default=18000, verbose_name='持续时间'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='level',
            field=models.IntegerField(default=1, verbose_name='比赛难度'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='lockboard',
            field=models.IntegerField(default=0, verbose_name='是否封榜'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='locktime',
            field=models.IntegerField(default=0, verbose_name='封榜时间'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='note',
            field=models.CharField(default='contest note', max_length=500, verbose_name='比赛提示'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='organizer',
            field=models.CharField(default='admin', max_length=50, verbose_name='组织人'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='priv',
            field=models.IntegerField(default=2, verbose_name='比赛权限'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='title',
            field=models.CharField(default='contest', max_length=50, verbose_name='比赛标题'),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='type',
            field=models.CharField(default='ACM', max_length=50, verbose_name='比赛赛制'),
        ),
        migrations.AlterField(
            model_name='contestplayer',
            name='contestid',
            field=models.IntegerField(verbose_name='比赛ID'),
        ),
        migrations.AlterField(
            model_name='contestplayer',
            name='user',
            field=models.CharField(max_length=50, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='contestproblem',
            name='contestid',
            field=models.IntegerField(verbose_name='比赛ID'),
        ),
        migrations.AlterField(
            model_name='contestproblem',
            name='problemid',
            field=models.CharField(max_length=50, verbose_name='题目ID'),
        ),
        migrations.AlterField(
            model_name='contestproblem',
            name='problemtitle',
            field=models.CharField(default='uname', max_length=500, verbose_name='题目标题'),
        ),
        migrations.AlterField(
            model_name='contestproblem',
            name='rank',
            field=models.IntegerField(verbose_name='题目序号'),
        ),
    ]
