# Generated by Django 3.2.19 on 2023-06-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0019_auto_20230627_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerd',
            name='url',
            field=models.CharField(max_length=256, verbose_name='镜像'),
        ),
    ]
