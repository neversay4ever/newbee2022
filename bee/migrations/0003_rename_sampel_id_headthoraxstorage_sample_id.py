# Generated by Django 3.2 on 2022-10-07 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0002_auto_20221007_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headthoraxstorage',
            old_name='sampel_id',
            new_name='sample_id',
        ),
    ]
