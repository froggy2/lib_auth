# Generated by Django 4.0 on 2021-12-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issued',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='issued',
            name='issue_date',
            field=models.DateField(auto_now=True),
        ),
    ]