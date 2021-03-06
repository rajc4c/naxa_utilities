# Generated by Django 2.2.10 on 2020-04-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_auto_20200408_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtdata',
            name='total_negative',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='districtdata',
            name='total_recovered',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total no Recovered निको भएको'),
        ),
        migrations.AddField(
            model_name='munidata',
            name='total_negative',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='munidata',
            name='total_recovered',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total no Recovered निको भएको'),
        ),
        migrations.AddField(
            model_name='munidata',
            name='total_samples_pending',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total No of Pending Cases (Test Pending)'),
        ),
    ]
