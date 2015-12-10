# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shanghaitech_SIST_db', '0004_auto_20150813_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='abstract_zh',
            new_name='abstract',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content_zh',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='point',
            old_name='name_zh',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='abstract_en',
        ),
        migrations.RemoveField(
            model_name='article',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='point',
            name='full_url',
        ),
        migrations.RemoveField(
            model_name='point',
            name='name_en',
        ),
    ]
