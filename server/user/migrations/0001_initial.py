# Generated by Django 4.2.11 on 2024-04-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oj_name', models.CharField(default='NOJ', max_length=100)),
                ('language', models.CharField(default='C++|C|Python3|Python2|Swift5.1|Java', max_length=500)),
                ('open_oi', models.BooleanField(default=True)),
                ('open_code', models.BooleanField(default=True)),
                ('open_visitor', models.BooleanField(default=True)),
                ('open_register', models.BooleanField(default=True)),
                ('open_testcase', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('reg_time', models.DateTimeField(auto_now=True)),
                ('qq', models.CharField(default='', max_length=50, null=True)),
                ('email', models.CharField(default='', max_length=50, null=True)),
                ('type', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('ip', models.CharField(default='unknow', max_length=50, null=True)),
                ('login_time', models.DateTimeField(auto_now=True)),
                ('msg', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ac', models.IntegerField(default=0)),
                ('submit', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('des', models.CharField(max_length=50, null=True)),
                ('rating', models.IntegerField(default=1500)),
                ('acpro', models.TextField(default='', null=True)),
            ],
        ),
    ]