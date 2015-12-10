# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shanghaitech_SIST_db', '0003_auto_20150728_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='template',
            field=models.CharField(verbose_name='渲染模板', default='a', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='point',
            name='type',
            field=models.IntegerField(verbose_name='节点类型', choices=[(0, '普通分支节点'), (2, '文章节点'), (3, '链接节点')]),
        ),
        migrations.DeleteModel(
            name='Tempelate',
        ),
    ]
