# Generated by Django 2.2.10 on 2020-04-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_auto_20200407_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerytaskprogress',
            name='task_type',
            field=models.IntegerField(choices=[(0, 'Generate User Report xlsx'), (1, 'Generate Facility Report xlsx')], default=0),
        ),
    ]
