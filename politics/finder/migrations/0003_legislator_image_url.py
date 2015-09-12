# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0002_auto_20150912_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislator',
            name='image_url',
            field=models.URLField(default='http://2.bp.blogspot.com/-6QyJDHjB5XE/Uscgo2DVBdI/AAAAAAAACS0/DFSFGLBK_fY/s1600/facebook-default-no-profile-pic.jpg'),
            preserve_default=False,
        ),
    ]
