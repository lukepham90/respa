# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-17 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respa_exchange', '0008_migrate_x500_address_data'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exchangeuser',
            unique_together=set([('exchange', 'email_address')]),
        ),
        migrations.RemoveField(
            model_name='exchangeuser',
            name='x500_address',
        ),
    ]