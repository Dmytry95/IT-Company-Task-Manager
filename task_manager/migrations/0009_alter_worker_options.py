# Generated by Django 4.2.2 on 2023-06-18 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0008_worker_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ['-position'], 'verbose_name': 'worker', 'verbose_name_plural': 'workers'},
        ),
    ]
