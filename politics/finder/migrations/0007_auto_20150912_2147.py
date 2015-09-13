# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0006_bill_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='short_title',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='bill',
            name='title',
            field=models.CharField(max_length=512),
        ),
    ]
