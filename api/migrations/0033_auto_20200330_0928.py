# Generated by Django 2.2.10 on 2020-03-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_mobileversion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='lat',
            field=models.FloatField(blank=True, default=27, null=True),
        ),
        migrations.AlterField(
            model_name='userlocation',
            name='long',
            field=models.FloatField(blank=True, default=85, null=True),
        ),
        migrations.AlterField(
            model_name='userreport',
            name='lat',
            field=models.FloatField(blank=True, default=27.61824026, null=True),
        ),
        migrations.AlterField(
            model_name='userreport',
            name='long',
            field=models.FloatField(blank=True, default=85.56, null=True),
        ),
    ]
