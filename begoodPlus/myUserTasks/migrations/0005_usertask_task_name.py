# Generated by Django 3.0.8 on 2021-02-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myUserTasks', '0004_auto_20210225_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='task_name',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
