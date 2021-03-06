# Generated by Django 2.2.5 on 2020-05-13 16:31

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeAlternates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(blank=True, max_length=300, null=True, verbose_name='Case Number')),
                ('case_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('project_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('cac', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('status', models.CharField(blank=True, max_length=300, null=True, verbose_name='Status')),
                ('contact', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact')),
                ('contact_url', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact URL')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Administrative Alternate Request',
            },
        ),
        migrations.CreateModel(
            name='CitizenAdvisoryCouncil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('cac', models.CharField(max_length=17)),
                ('name', models.CharField(max_length=17)),
                ('cac_code', models.CharField(max_length=1)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrape', models.BooleanField(default=True)),
                ('scan', models.BooleanField(default=True)),
                ('notify', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='coverArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Name')),
                ('CACs', models.ManyToManyField(to='develop.CitizenAdvisoryCouncil')),
            ],
            options={
                'verbose_name': 'Cover Area',
            },
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OBJECTID', models.IntegerField(verbose_name='Object ID')),
                ('devplan_id', models.IntegerField(blank=True, null=True, verbose_name='Development Plan ID')),
                ('submitted', models.BigIntegerField(blank=True, null=True, verbose_name='Submitted')),
                ('submitted_yr', models.SmallIntegerField(blank=True, null=True, verbose_name='Year Submitted')),
                ('approved', models.BigIntegerField(blank=True, null=True, verbose_name='Approved')),
                ('daystoapprove', models.IntegerField(blank=True, null=True, verbose_name='Days to Approve')),
                ('plan_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan Type')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('appealperiodends', models.BigIntegerField(blank=True, null=True, verbose_name='Appeal Period Ends')),
                ('updated', models.BigIntegerField(blank=True, null=True, verbose_name='Updated')),
                ('sunset_date', models.BigIntegerField(blank=True, null=True, verbose_name='Sunset Date')),
                ('acreage', models.CharField(blank=True, max_length=100, null=True, verbose_name='Acreage')),
                ('major_street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Major Street')),
                ('cac', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('engineer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Engineer')),
                ('engineer_phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Engineer Phone')),
                ('developer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Developer')),
                ('developer_phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Developer Phone')),
                ('plan_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('planurl', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('planurl_approved', models.TextField(blank=True, null=True, verbose_name='Plan URL Approved')),
                ('planner', models.CharField(blank=True, max_length=100, null=True, verbose_name='Planner')),
                ('lots_req', models.IntegerField(blank=True, null=True, verbose_name='Lots Req')),
                ('lots_rec', models.IntegerField(blank=True, null=True, verbose_name='Lots Rec')),
                ('lots_apprv', models.IntegerField(blank=True, null=True, verbose_name='Lots Approved')),
                ('sq_ft_req', models.IntegerField(blank=True, null=True, verbose_name='Square Feet Req')),
                ('units_apprv', models.IntegerField(blank=True, null=True, verbose_name='Units Approved')),
                ('units_req', models.IntegerField(blank=True, null=True, verbose_name='Units Req')),
                ('zoning', models.CharField(blank=True, max_length=100, null=True, verbose_name='Zoning')),
                ('plan_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan Number')),
                ('CreationDate', models.BigIntegerField(blank=True, null=True, verbose_name='Creation Date')),
                ('Creator', models.CharField(blank=True, max_length=100, null=True, verbose_name='Creator')),
                ('EditDate', models.BigIntegerField(blank=True, null=True, verbose_name='Edit Date')),
                ('Editor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Editor')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Development',
            },
        ),
        migrations.CreateModel(
            name='SiteReviewCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Case Number')),
                ('case_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('project_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('cac', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact')),
                ('contact_url', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact URL')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Site Review Case',
            },
        ),
        migrations.CreateModel(
            name='TextChangeCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Case Number')),
                ('case_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('project_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact')),
                ('contact_url', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact URL')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Text Change Case',
            },
        ),
        migrations.CreateModel(
            name='WakeCorporate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('short_name', models.CharField(max_length=3)),
                ('long_name', models.CharField(max_length=13)),
                ('ordinance_field', models.CharField(max_length=18)),
                ('effective_field', models.CharField(max_length=24)),
                ('shapearea', models.FloatField()),
                ('shapelen', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Zoning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OBJECTID', models.IntegerField(blank=True, null=True, verbose_name='Object ID')),
                ('zpyear', models.SmallIntegerField(blank=True, null=True, verbose_name='Year Submitted')),
                ('zpnum', models.SmallIntegerField(blank=True, null=True, verbose_name='Zoning Number')),
                ('submittal_date', models.BigIntegerField(blank=True, null=True, verbose_name='Submitted')),
                ('petitioner', models.CharField(blank=True, max_length=300, null=True, verbose_name='Petitioner')),
                ('location', models.CharField(blank=True, max_length=300, null=True, verbose_name='Location')),
                ('remarks', models.CharField(blank=True, max_length=300, null=True, verbose_name='Remarks')),
                ('zp_petition_acres', models.CharField(blank=True, max_length=100, null=True, verbose_name='Acreage')),
                ('planning_commission_action', models.CharField(blank=True, max_length=300, null=True, verbose_name='PC Action')),
                ('city_council_action', models.CharField(blank=True, max_length=300, null=True, verbose_name='CC Action')),
                ('ph_date', models.BigIntegerField(blank=True, null=True, verbose_name='PH Date')),
                ('withdraw_date', models.BigIntegerField(blank=True, null=True, verbose_name='Withdraw Date')),
                ('exp_date_120_days', models.BigIntegerField(blank=True, null=True, verbose_name='Exp Date 120 Days')),
                ('exp_date_2_year', models.BigIntegerField(blank=True, null=True, verbose_name='Exp Date 2 Year')),
                ('ordinance_number', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ordinance Number')),
                ('received_by', models.CharField(blank=True, max_length=300, null=True, verbose_name='Received By')),
                ('last_revised', models.CharField(blank=True, max_length=300, null=True, verbose_name='Last Revised')),
                ('drain_basin', models.CharField(blank=True, max_length=300, null=True, verbose_name='Drain Basin')),
                ('cac', models.CharField(blank=True, max_length=300, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('comprehensive_plan_districts', models.CharField(blank=True, max_length=300, null=True, verbose_name='Comprehensive Plan Districts')),
                ('GlobalID', models.CharField(blank=True, max_length=300, null=True, verbose_name='Global ID')),
                ('CreationDate', models.BigIntegerField(blank=True, null=True, verbose_name='Creation Date')),
                ('EditDate', models.BigIntegerField(blank=True, null=True, verbose_name='Edit Date')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, max_length=300, null=True, verbose_name='Status')),
                ('plan_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('location_url', models.TextField(blank=True, null=True, verbose_name='Location URL')),
            ],
            options={
                'verbose_name': 'Zoning Request',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Subscribed')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('send_emails', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('topic_id', models.IntegerField(blank=True, null=True, verbose_name='Topic ID')),
                ('api_key', models.CharField(blank=True, max_length=254, null=True)),
                ('cover_areas', models.ManyToManyField(to='develop.coverArea')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalZoning',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('OBJECTID', models.IntegerField(blank=True, null=True, verbose_name='Object ID')),
                ('zpyear', models.SmallIntegerField(blank=True, null=True, verbose_name='Year Submitted')),
                ('zpnum', models.SmallIntegerField(blank=True, null=True, verbose_name='Zoning Number')),
                ('submittal_date', models.BigIntegerField(blank=True, null=True, verbose_name='Submitted')),
                ('petitioner', models.CharField(blank=True, max_length=300, null=True, verbose_name='Petitioner')),
                ('location', models.CharField(blank=True, max_length=300, null=True, verbose_name='Location')),
                ('remarks', models.CharField(blank=True, max_length=300, null=True, verbose_name='Remarks')),
                ('zp_petition_acres', models.CharField(blank=True, max_length=100, null=True, verbose_name='Acreage')),
                ('planning_commission_action', models.CharField(blank=True, max_length=300, null=True, verbose_name='PC Action')),
                ('city_council_action', models.CharField(blank=True, max_length=300, null=True, verbose_name='CC Action')),
                ('ph_date', models.BigIntegerField(blank=True, null=True, verbose_name='PH Date')),
                ('withdraw_date', models.BigIntegerField(blank=True, null=True, verbose_name='Withdraw Date')),
                ('exp_date_120_days', models.BigIntegerField(blank=True, null=True, verbose_name='Exp Date 120 Days')),
                ('exp_date_2_year', models.BigIntegerField(blank=True, null=True, verbose_name='Exp Date 2 Year')),
                ('ordinance_number', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ordinance Number')),
                ('received_by', models.CharField(blank=True, max_length=300, null=True, verbose_name='Received By')),
                ('last_revised', models.CharField(blank=True, max_length=300, null=True, verbose_name='Last Revised')),
                ('drain_basin', models.CharField(blank=True, max_length=300, null=True, verbose_name='Drain Basin')),
                ('cac', models.CharField(blank=True, max_length=300, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('comprehensive_plan_districts', models.CharField(blank=True, max_length=300, null=True, verbose_name='Comprehensive Plan Districts')),
                ('GlobalID', models.CharField(blank=True, max_length=300, null=True, verbose_name='Global ID')),
                ('CreationDate', models.BigIntegerField(blank=True, null=True, verbose_name='Creation Date')),
                ('EditDate', models.BigIntegerField(blank=True, null=True, verbose_name='Edit Date')),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('status', models.CharField(blank=True, max_length=300, null=True, verbose_name='Status')),
                ('plan_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('location_url', models.TextField(blank=True, null=True, verbose_name='Location URL')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Zoning Request',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTextChangeCases',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('case_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Case Number')),
                ('case_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('project_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact')),
                ('contact_url', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact URL')),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Text Change Case',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSiteReviewCases',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('case_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Case Number')),
                ('case_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('project_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('cac', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact')),
                ('contact_url', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact URL')),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Site Review Case',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDevelopment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('OBJECTID', models.IntegerField(verbose_name='Object ID')),
                ('devplan_id', models.IntegerField(blank=True, null=True, verbose_name='Development Plan ID')),
                ('submitted', models.BigIntegerField(blank=True, null=True, verbose_name='Submitted')),
                ('submitted_yr', models.SmallIntegerField(blank=True, null=True, verbose_name='Year Submitted')),
                ('approved', models.BigIntegerField(blank=True, null=True, verbose_name='Approved')),
                ('daystoapprove', models.IntegerField(blank=True, null=True, verbose_name='Days to Approve')),
                ('plan_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan Type')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('appealperiodends', models.BigIntegerField(blank=True, null=True, verbose_name='Appeal Period Ends')),
                ('updated', models.BigIntegerField(blank=True, null=True, verbose_name='Updated')),
                ('sunset_date', models.BigIntegerField(blank=True, null=True, verbose_name='Sunset Date')),
                ('acreage', models.CharField(blank=True, max_length=100, null=True, verbose_name='Acreage')),
                ('major_street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Major Street')),
                ('cac', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('engineer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Engineer')),
                ('engineer_phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Engineer Phone')),
                ('developer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Developer')),
                ('developer_phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Developer Phone')),
                ('plan_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('planurl', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('planurl_approved', models.TextField(blank=True, null=True, verbose_name='Plan URL Approved')),
                ('planner', models.CharField(blank=True, max_length=100, null=True, verbose_name='Planner')),
                ('lots_req', models.IntegerField(blank=True, null=True, verbose_name='Lots Req')),
                ('lots_rec', models.IntegerField(blank=True, null=True, verbose_name='Lots Rec')),
                ('lots_apprv', models.IntegerField(blank=True, null=True, verbose_name='Lots Approved')),
                ('sq_ft_req', models.IntegerField(blank=True, null=True, verbose_name='Square Feet Req')),
                ('units_apprv', models.IntegerField(blank=True, null=True, verbose_name='Units Approved')),
                ('units_req', models.IntegerField(blank=True, null=True, verbose_name='Units Req')),
                ('zoning', models.CharField(blank=True, max_length=100, null=True, verbose_name='Zoning')),
                ('plan_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan Number')),
                ('CreationDate', models.BigIntegerField(blank=True, null=True, verbose_name='Creation Date')),
                ('Creator', models.CharField(blank=True, max_length=100, null=True, verbose_name='Creator')),
                ('EditDate', models.BigIntegerField(blank=True, null=True, verbose_name='Edit Date')),
                ('Editor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Editor')),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Development',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAdministrativeAlternates',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('case_number', models.CharField(blank=True, max_length=300, null=True, verbose_name='Case Number')),
                ('case_url', models.TextField(blank=True, null=True, verbose_name='Plan URL')),
                ('project_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Plan Name')),
                ('cac', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC')),
                ('cac_override', models.CharField(blank=True, max_length=100, null=True, verbose_name='CAC Override')),
                ('status', models.CharField(blank=True, max_length=300, null=True, verbose_name='Status')),
                ('contact', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact')),
                ('contact_url', models.CharField(blank=True, max_length=300, null=True, verbose_name='Contact URL')),
                ('created_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Administrative Alternate Request',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
