# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(null=True, max_length=200)),
                ('number', models.IntegerField()),
                ('chamber', models.CharField(choices=[('h', 'House'), ('s', 'Senate')], max_length=10)),
                ('bill_type', models.CharField(max_length=255)),
                ('bill_id', models.CharField(unique=True, max_length=255)),
                ('opencongress_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Legislator',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('bioguide_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('congress_image_url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('vote', models.CharField(choices=[('Yea', 'Yea'), ('Nay', 'Nay'), ('Not Voting', 'Not Voting'), ('Not Present', 'Not Present')], default='Not Present', max_length=255)),
                ('bill', models.ForeignKey(to='finder.Bill')),
                ('legislator', models.ForeignKey(to='finder.Legislator')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='sponsor',
            field=models.ForeignKey(to='finder.Legislator'),
        ),
    ]
