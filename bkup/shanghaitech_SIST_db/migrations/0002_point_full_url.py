# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shanghaitech_SIST_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='full_url',
            field=models.CharField(max_length=255, default=0, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
