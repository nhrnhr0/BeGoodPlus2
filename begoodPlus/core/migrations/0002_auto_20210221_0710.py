# Generated by Django 3.0.8 on 2021-02-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besecontactinformation',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True, verbose_name='אימייל'),
        ),
        migrations.AlterField(
            model_name='besecontactinformation',
            name='message',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='הודעה'),
        ),
        migrations.AlterField(
            model_name='besecontactinformation',
            name='name',
            field=models.CharField(max_length=50, verbose_name='שם'),
        ),
        migrations.AlterField(
            model_name='besecontactinformation',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='phone'),
        ),
    ]