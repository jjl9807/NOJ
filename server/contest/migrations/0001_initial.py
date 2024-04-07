# Generated by Django 4.2.11 on 2024-04-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContestAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestid', models.IntegerField()),
                ('announcement', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContestBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestid', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('problemrank', models.IntegerField()),
                ('type', models.IntegerField()),
                ('submittime', models.BigIntegerField()),
                ('submitid', models.IntegerField()),
                ('rating', models.IntegerField(default=1500)),
            ],
        ),
        migrations.CreateModel(
            name='ContestBoardTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('contestid', models.IntegerField()),
                ('score', models.IntegerField()),
                ('time', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContestInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.CharField(default='admin', max_length=50)),
                ('oj', models.CharField(default='LPOJ', max_length=50)),
                ('title', models.CharField(default='contest', max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('des', models.CharField(default='contest des', max_length=500)),
                ('note', models.CharField(default='contest note', max_length=500)),
                ('begintime', models.DateTimeField()),
                ('lasttime', models.IntegerField(default=18000)),
                ('type', models.CharField(default='ACM', max_length=50)),
                ('priv', models.IntegerField(default=2)),
                ('iprange', models.CharField(default='iprange', max_length=2000)),
                ('lockboard', models.IntegerField(default=0)),
                ('locktime', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ContestPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestid', models.IntegerField()),
                ('user', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ContestProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestid', models.IntegerField()),
                ('problemid', models.CharField(max_length=50)),
                ('problemtitle', models.CharField(default='uname', max_length=500)),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
