# Generated by Django 2.2.5 on 2020-05-18 00:45

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('develop', '0004_auto_20200517_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waketownship',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=0),
        ),
    ]