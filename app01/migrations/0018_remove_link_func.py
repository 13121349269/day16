# Generated by Django 3.2.19 on 2023-06-27 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_containerd_link_middleware_servers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='func',
        ),
    ]
