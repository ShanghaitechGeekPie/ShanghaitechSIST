# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shanghaitech_SIST_db', '0002_point_full_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='tempelate',
            new_name='template',
        ),
    ]
