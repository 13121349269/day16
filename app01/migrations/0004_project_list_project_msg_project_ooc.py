# Generated by Django 3.2.19 on 2023-06-16 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_prettynum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=64, verbose_name='项目名称')),
                ('change_time', models.DateField(verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Ooc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_doc', models.FileField(null=True, upload_to='upload_files')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.project_list', verbose_name='项目ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_coe', models.CharField(max_length=64, verbose_name='项目编码')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.project_list', verbose_name='项目ID')),
            ],
        ),
    ]
