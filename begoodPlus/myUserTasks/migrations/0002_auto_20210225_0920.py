# Generated by Django 3.0.8 on 2021-02-25 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('myUserTasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.Session'),
        ),
        migrations.DeleteModel(
            name='UserTasks',
        ),
    ]
