# Generated by Django 3.1.3 on 2022-06-04 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_merge_20210127_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 16, 50, 5, 720874)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 16, 50, 5, 720874)),
        ),
    ]
