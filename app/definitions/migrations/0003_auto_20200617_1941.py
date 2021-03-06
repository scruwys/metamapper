# Generated by Django 3.0.7 on 2020-06-17 19:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('definitions', '0002_auto_20200526_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastore',
            name='disabled_datastore_properties',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=list, size=None),
        ),
        migrations.AddField(
            model_name='datastore',
            name='disabled_table_properties',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=list, size=None),
        ),
    ]
