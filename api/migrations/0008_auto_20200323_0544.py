# Generated by Django 2.2.10 on 2020-03-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_province_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='province_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]