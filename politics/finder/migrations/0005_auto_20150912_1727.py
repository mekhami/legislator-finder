# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_auto_20150912_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legislator',
            name='twitter_id',
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='twitter_image_url',
        ),
    ]
