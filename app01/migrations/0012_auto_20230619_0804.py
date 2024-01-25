# Generated by Django 3.2.19 on 2023-06-19 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20230619_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_doc',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.project_list', verbose_name='项目名'),
        ),
        migrations.AlterField(
            model_name='project_msg',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.project_list', verbose_name='项目名'),
        ),
    ]