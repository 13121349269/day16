# Generated by Django 3.2.19 on 2024-01-24 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0029_alter_userinfo_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_doc',
            name='upload',
        ),
    ]
