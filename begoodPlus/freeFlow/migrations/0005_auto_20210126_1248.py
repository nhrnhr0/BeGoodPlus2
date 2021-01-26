# Generated by Django 3.0.8 on 2021-01-26 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freeFlow', '0004_freeflowcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeflowcontent',
            name='nav_AboutUs',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freeflowcontent',
            name='nav_BenefitsAdvantages',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freeflowcontent',
            name='nav_Home',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freeflowcontent',
            name='nav_Videos',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
