# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('spread', models.FloatField()),
                ('XBTZAR', models.FloatField()),
                ('XBTUSD', models.FloatField()),
                ('USDZAR', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tick',
                'verbose_name_plural': 'Ticks',
            },
        ),
    ]
