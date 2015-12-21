# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='icons')),
                ('extended_object', models.OneToOneField(to='cms.Page', editable=False)),
                ('public_extension', models.OneToOneField(to='testss.IconExtension', related_name='draft_extension', editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
