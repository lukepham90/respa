# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-08 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0069_unit_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='parent_reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_reservations', to='resources.Reservation', verbose_name='Parent reservation'),
        ),
        migrations.AddField(
            model_name='resource',
            name='child_resources',
            field=models.ManyToManyField(blank=True, related_name='parent_resources', to='resources.Resource', verbose_name='Child resources'),
        ),
    ]
