# Generated by Django 3.2.19 on 2023-10-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0026_auto_20231031_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='project_name',
            field=models.CharField(default=1, max_length=32, verbose_name='关联项目'),
            preserve_default=False,
        ),
    ]
