# Generated by Django 3.0.8 on 2021-01-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeFlow', '0008_auto_20210126_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeflowclient',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='תאריך יצירה'),
        ),
        migrations.AlterField(
            model_name='freeflowclient',
            name='message',
            field=models.CharField(max_length=200, verbose_name='הודעה'),
        ),
    ]
