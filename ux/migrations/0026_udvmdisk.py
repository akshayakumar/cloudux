# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ux', '0025_udvdc'),
    ]

    operations = [
        migrations.CreateModel(
            name='UdVmDisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dbstatus', models.CharField(default=b'A', max_length=1)),
                ('vm_name', models.CharField(blank=True, max_length=100, null=True)),
                ('datacenter_name', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_number', models.IntegerField(default=0)),
                ('disk_id', models.CharField(blank=True, max_length=200, null=True)),
                ('provision_size_gb', models.CharField(blank=True, max_length=10, null=True)),
                ('vm_id', models.CharField(blank=True, max_length=100, null=True)),
                ('datastore_name', models.CharField(blank=True, max_length=100, null=True)),
                ('disk_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]