# Generated by Django 3.0.8 on 2021-01-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeFlow', '0005_auto_20210126_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeflowcontent',
            name='nav_ContactUs',
            field=models.CharField(default='Contact Us', max_length=100),
            preserve_default=False,
        ),
    ]
