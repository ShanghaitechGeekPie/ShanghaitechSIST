# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('abstract_zh', models.TextField(verbose_name='文章摘要', blank=True)),
                ('abstract_en', models.TextField(verbose_name='Abstract', blank=True)),
                ('content_zh', models.TextField(verbose_name='文章内容', blank=True)),
                ('content_en', models.TextField(verbose_name='Content', blank=True)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name_zh', models.CharField(max_length=255, verbose_name='节点名称', blank=True)),
                ('name_en', models.CharField(max_length=255, verbose_name='Point Name', blank=True)),
                ('url', models.CharField(max_length=255, verbose_name='URL段')),
                ('type', models.IntegerField(choices=[(1, '分支节点'), (2, '文章节点'), (3, '链接节点')], verbose_name='节点类型')),
                ('foreignkey_article', models.ForeignKey(blank=True, verbose_name='文章对象', null=True, to='shanghaitech_SIST_db.Article')),
                ('parent', models.ForeignKey(blank=True, verbose_name='上级节点', null=True, to='shanghaitech_SIST_db.Point')),
            ],
        ),
        migrations.CreateModel(
            name='Tempelate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='模板名称')),
                ('address', models.CharField(max_length=255, verbose_name='模板地址')),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='tempelate',
            field=models.ForeignKey(blank=True, verbose_name='渲染模板', null=True, to='shanghaitech_SIST_db.Tempelate'),
        ),
    ]
