# Generated by Django 2.2.10 on 2020-04-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_auto_20200404_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincedata',
            name='total_death',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total No Deaths (मृत्यु भएको)'),
        ),
        migrations.AlterField(
            model_name='provincedata',
            name='total_in_isolation',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total No in Isolations (आइसोलेसनमा)'),
        ),
        migrations.AlterField(
            model_name='provincedata',
            name='total_negative',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total Negetive (संक्रमण नदेखिएको)'),
        ),
        migrations.AlterField(
            model_name='provincedata',
            name='total_positive',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total No of +ve Infections (संक्रमण देखिएको)'),
        ),
        migrations.AlterField(
            model_name='provincedata',
            name='total_recovered',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total no Recovered निको भएको'),
        ),
        migrations.AlterField(
            model_name='provincedata',
            name='total_samples_collected',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total No. of Samples Collected (नमुना संकलन गरिएको)'),
        ),
        migrations.AlterField(
            model_name='provincedata',
            name='total_samples_pending',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total No of Pending Cases (Test Pending)'),
        ),
        migrations.AlterField(
            model_name='provincedata',
            name='total_tested',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total No. of Samples Examined (परिक्षण गरिएको)'),
        ),
    ]