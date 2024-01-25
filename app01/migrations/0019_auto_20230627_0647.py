# Generated by Django 3.2.19 on 2023-06-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0018_remove_link_func'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerd',
            name='port',
            field=models.CharField(max_length=12, null=True, verbose_name='端口'),
        ),
        migrations.AddField(
            model_name='containerd',
            name='version',
            field=models.CharField(max_length=12, null=True, verbose_name='版本'),
        ),
    ]