# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='short_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='title',
            field=models.TextField(),
        ),
    ]
