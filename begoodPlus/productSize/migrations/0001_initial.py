# Generated by Django 3.0.8 on 2020-11-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='X', max_length=30, unique=True, verbose_name='גודל')),
                ('code', models.CharField(default=0, max_length=2, verbose_name='קוד')),
            ],
            options={
                'verbose_name': 'גודל מוצר',
                'verbose_name_plural': 'גדלי מוצרים',
                'ordering': ('code',),
                'default_related_name': 'productSizes',
            },
        ),
    ]