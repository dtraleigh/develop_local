# Generated by Django 2.2.5 on 2020-05-18 00:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0006_delete_waketownship'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('short_name', models.CharField(max_length=3)),
                ('long_name', models.CharField(max_length=13)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
