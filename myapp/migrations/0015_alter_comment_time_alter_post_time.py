# Generated by Django 4.1.7 on 2023-12-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(blank=True, default='23 December 2023', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.CharField(blank=True, default='23 December 2023', max_length=100),
        ),
    ]
