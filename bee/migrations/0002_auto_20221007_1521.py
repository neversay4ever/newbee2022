# Generated by Django 3.2 on 2022-10-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beeall',
            name='geo_notes',
            field=models.TextField(blank=True, null=True, verbose_name='采集地备注'),
        ),
        migrations.AlterField(
            model_name='collectiondata',
            name='geo_notes',
            field=models.TextField(blank=True, null=True, verbose_name='采集地备注'),
        ),
    ]
