# Generated by Django 4.0 on 2021-12-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0004_rename_location_profile_bits_id_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hostel',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='room_no',
            field=models.IntegerField(null=True),
        ),
    ]