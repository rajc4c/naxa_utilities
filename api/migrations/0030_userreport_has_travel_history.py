# Generated by Django 2.2.10 on 2020-03-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_userreport_has_convid_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreport',
            name='has_travel_history',
            field=models.BooleanField(default=False),
        ),
    ]
