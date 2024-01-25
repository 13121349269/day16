# Generated by Django 3.2.19 on 2023-06-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_alter_project_doc_project_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Containerd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='服务名')),
                ('url', models.CharField(max_length=64, verbose_name='镜像')),
                ('date', models.DateField(max_length=64, verbose_name='更新时间')),
                ('other_1', models.CharField(max_length=32, null=True, verbose_name='备注1')),
                ('other_2', models.CharField(max_length=32, null=True, verbose_name='备注2')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.CharField(max_length=12, null=True, verbose_name='用途')),
                ('name', models.CharField(max_length=64, verbose_name='链接名')),
                ('link', models.CharField(max_length=128, verbose_name='链接')),
                ('user_name', models.CharField(max_length=12, null=True, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=32, null=True, verbose_name='密码')),
                ('other_1', models.CharField(max_length=32, null=True, verbose_name='备注1')),
                ('other_2', models.CharField(max_length=32, null=True, verbose_name='备注2')),
            ],
        ),
        migrations.CreateModel(
            name='Middleware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=12, verbose_name='类型')),
                ('name', models.CharField(max_length=12, verbose_name='服务名')),
                ('func', models.CharField(max_length=32, null=True, verbose_name='功能')),
                ('version', models.CharField(max_length=12, null=True, verbose_name='版本')),
                ('hostname', models.CharField(max_length=12, null=True, verbose_name='主机名')),
                ('public_network', models.CharField(max_length=12, null=True, verbose_name='公网链接方式')),
                ('public_port', models.CharField(max_length=12, null=True, verbose_name='公网端口')),
                ('intranet', models.CharField(max_length=12, null=True, verbose_name='内网链接方式')),
                ('intranet_port', models.CharField(max_length=12, null=True, verbose_name='内网端口')),
                ('username', models.CharField(max_length=12, null=True, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=32, null=True, verbose_name='密码')),
                ('install_path', models.CharField(max_length=128, null=True, verbose_name='安装路径')),
                ('data_paht', models.CharField(max_length=128, null=True, verbose_name='数据路径')),
                ('start_command', models.CharField(max_length=128, null=True, verbose_name='启动命令')),
                ('other_1', models.CharField(max_length=32, null=True, verbose_name='备注1')),
                ('other_2', models.CharField(max_length=32, null=True, verbose_name='备注2')),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32, null=True, verbose_name='类型')),
                ('os', models.CharField(max_length=32, null=True, verbose_name='系统版本')),
                ('hostname', models.CharField(max_length=32, null=True, verbose_name='实例名')),
                ('func', models.CharField(max_length=32, null=True, verbose_name='用途')),
                ('public_ip', models.CharField(max_length=32, null=True, verbose_name='外网IP')),
                ('intranet_ip', models.CharField(max_length=32, null=True, verbose_name='内网ip')),
                ('username', models.CharField(max_length=32, null=True, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=32, null=True, verbose_name='密码')),
                ('sshport', models.CharField(max_length=12, null=True, verbose_name='ssh端口')),
                ('CPU', models.CharField(max_length=12, null=True, verbose_name='cpu')),
                ('memory', models.CharField(max_length=12, null=True, verbose_name='内存')),
                ('server_disk', models.CharField(max_length=12, null=True, verbose_name='系统盘')),
                ('data_disk', models.CharField(max_length=12, null=True, verbose_name='数据盘')),
                ('disk_type', models.CharField(max_length=12, null=True, verbose_name='磁盘类型')),
                ('host_type', models.CharField(max_length=12, null=True, verbose_name='机器类型')),
                ('other_1', models.CharField(max_length=32, null=True, verbose_name='备注1')),
                ('other_2', models.CharField(max_length=32, null=True, verbose_name='备注2')),
            ],
        ),
    ]