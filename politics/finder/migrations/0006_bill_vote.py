# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0005_auto_20150912_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=256)),
                ('number', models.IntegerField()),
                ('chamber', models.CharField(choices=[('h', 'House'), ('s', 'Senate')], max_length=1)),
                ('bill_type', models.CharField(max_length=16)),
                ('bill_id', models.CharField(max_length=20)),
                ('opencongress_url', models.URLField()),
                ('sponsor', models.ForeignKey(to='finder.Legislator')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vote', models.CharField(choices=[('Yea', 'Yea'), ('Nay', 'Nay'), ('Not Voting', 'Not Voting'), ('Not Present', 'Not Present')], max_length=12, default='Not Present')),
                ('date', models.DateField()),
                ('bill', models.ForeignKey(to='finder.Bill')),
                ('legislator', models.ForeignKey(to='finder.Legislator')),
            ],
        ),
    ]
