# Generated by Django 4.2.11 on 2024-03-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('pid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('author', models.CharField(default='admin', max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500)),
                ('desc', models.TextField()),
                ('in_desc', models.TextField()),
                ('out_desc', models.TextField()),
                ('in_sample', models.TextField()),
                ('out_sample', models.TextField()),
                ('time_limit', models.IntegerField()),
                ('mem_limit', models.IntegerField()),
                ('hint', models.TextField(default='', null=True)),
                ('priv', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemMeta',
            fields=[
                ('pid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('level', models.IntegerField(default=1)),
                ('submission', models.IntegerField(default=0)),
                ('ac', models.IntegerField(default=0)),
                ('mle', models.IntegerField(default=0)),
                ('tle', models.IntegerField(default=0)),
                ('rte', models.IntegerField(default=0)),
                ('pe', models.IntegerField(default=0)),
                ('ce', models.IntegerField(default=0)),
                ('wa', models.IntegerField(default=0)),
                ('se', models.IntegerField(default=0)),
                ('tag', models.TextField(null=True)),
                ('score', models.IntegerField(default=100)),
                ('priv', models.IntegerField(default=1)),
                ('oj', models.CharField(default='LPOJ', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=50, unique=True)),
                ('num', models.IntegerField()),
            ],
        ),
    ]