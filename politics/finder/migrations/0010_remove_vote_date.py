# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0009_auto_20150912_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='date',
        ),
    ]
