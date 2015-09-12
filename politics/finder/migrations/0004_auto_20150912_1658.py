# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_legislator_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legislator',
            old_name='image_url',
            new_name='twitter_image_url',
        ),
        migrations.AddField(
            model_name='legislator',
            name='congress_image_url',
            field=models.URLField(default='none'),
            preserve_default=False,
        ),
    ]
