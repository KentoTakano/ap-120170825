# Generated by Django 2.0.3 on 2018-03-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0006_auto_20180317_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='race_data',
            name='day',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='race_data',
            name='month',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='race_data',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
