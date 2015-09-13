# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0007_auto_20150912_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
