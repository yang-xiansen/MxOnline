# Generated by Django 2.0.2 on 2018-04-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20180420_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='', max_length=20, verbose_name='课程类别'),
        ),
    ]