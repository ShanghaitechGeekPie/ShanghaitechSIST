# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shanghaitech_SIST_db', '0005_auto_20150911_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='view',
            field=models.BooleanField(verbose_name='View', default=False),
        ),
    ]
