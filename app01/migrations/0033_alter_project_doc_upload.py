# Generated by Django 3.2.19 on 2024-01-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0032_alter_project_doc_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_doc',
            name='upload',
            field=models.FileField(upload_to='project_doc/'),
        ),
    ]
