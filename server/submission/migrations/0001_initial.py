# Generated by Django 4.2.11 on 2024-04-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_id', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('problem', models.CharField(max_length=50)),
                ('result', models.CharField(default='System Error', max_length=500)),
                ('time', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('testcase', models.CharField(default='unknow', max_length=500)),
                ('casedata', models.CharField(max_length=500)),
                ('outputdata', models.CharField(default='', max_length=500)),
                ('useroutput', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('problem', models.CharField(max_length=50)),
                ('result', models.IntegerField()),
                ('time', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('length', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('submit_time', models.DateTimeField()),
                ('judger', models.CharField(max_length=50)),
                ('contest', models.IntegerField()),
                ('contest_problem', models.IntegerField(default=-1)),
                ('code', models.TextField(max_length=200000)),
                ('error_case', models.CharField(default='0', max_length=50)),
                ('message', models.TextField()),
                ('problem_title', models.CharField(default='', max_length=100)),
                ('ip', models.CharField(default='无法获取ip', max_length=50)),
            ],
        ),
    ]