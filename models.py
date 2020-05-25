from django.db import models
from django.contrib.gis.db import models

from simple_history.models import HistoricalRecords


class Control(models.Model):
    scrape = models.BooleanField(default=True)
    scan = models.BooleanField(default=True)
    notify = models.BooleanField(default=True)


class CitizenAdvisoryCouncil(models.Model):
    objectid = models.IntegerField()
    cac = models.CharField(max_length=17)
    name = models.CharField(max_length=17)
    cac_code = models.CharField(max_length=1)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


citizenadvisorycouncil_mapping = {
    'objectid': 'OBJECTID',
    'cac': 'CAC',
    'name': 'NAME',
    'cac_code': 'CAC_CODE',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}


class WakeCorporate(models.Model):
    objectid = models.IntegerField()
    short_name = models.CharField(max_length=3)
    long_name = models.CharField(max_length=13)
    ordinance_field = models.CharField(max_length=18)
    effective_field = models.CharField(max_length=24)
    shapearea = models.FloatField()
    shapelen = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.long_name


wakecorporate_mapping = {
    'objectid': 'OBJECTID',
    'short_name': 'SHORT_NAME',
    'long_name': 'LONG_NAME',
    'ordinance_field': 'ORDINANCE_',
    'effective_field': 'EFFECTIVE_',
    'shapearea': 'SHAPEAREA',
    'shapelen': 'SHAPELEN',
    'geom': 'MULTIPOLYGON',
}


class TrackArea(models.Model):
    objectid = models.IntegerField()
    short_name = models.CharField(max_length=3)
    long_name = models.CharField(max_length=13)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.long_name


trackarea_mapping = {
    'objectid': 'OBJECTID',
    'short_name': 'SHORT_NAME',
    'long_name': 'LONG_NAME',
    'geom': 'MULTIPOLYGON',
}


class coverArea(models.Model):
    name = models.CharField(blank=True, max_length=300, null=True, verbose_name="Name")
    CACs = models.ManyToManyField(CitizenAdvisoryCouncil)

    class Meta:
        verbose_name = "Cover Area"

    def __str__(self):
        return u"%s" % self.name


class Subscriber(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Subscribed")
    name = models.CharField(max_length=254)
    email = models.EmailField(unique=True)
    send_emails = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    cover_areas = models.ManyToManyField(coverArea)
    is_bot = models.BooleanField(default=False)
    topic_id = models.IntegerField(blank=True, null=True, verbose_name="Topic ID")
    api_key = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return u"%s (%s)" % (self.name, self.email)


class DevelopmentPlan(models.Model):
    objectid = models.IntegerField()
    devplan_id = models.IntegerField()
    submitted = models.DateField()
    submitted_field = models.IntegerField()
    approved = models.DateField()
    daystoappr = models.IntegerField()
    plan_type = models.CharField(max_length=39)
    status = models.CharField(max_length=18)
    appealperi = models.DateField()
    updated = models.DateField()
    sunset_dat = models.DateField()
    acreage = models.FloatField()
    major_stre = models.CharField(max_length=31)
    cac = models.CharField(max_length=18)
    engineer = models.CharField(max_length=35)
    engineer_p = models.CharField(max_length=10)
    developer = models.CharField(max_length=48)
    developer_field = models.CharField(max_length=13)
    plan_name = models.CharField(max_length=44)
    planurl = models.CharField(max_length=107)
    planurl_ap = models.CharField(max_length=1)
    planner = models.CharField(max_length=30)
    lots_req = models.IntegerField()
    lots_rec = models.IntegerField()
    lots_apprv = models.IntegerField()
    sq_ft_req = models.IntegerField()
    units_appr = models.IntegerField()
    units_req = models.IntegerField()
    zoning = models.CharField(max_length=34)
    plan_numbe = models.CharField(max_length=15)
    creationda = models.DateField()
    creator = models.CharField(max_length=12)
    editdate = models.DateField()
    editor = models.CharField(max_length=12)
    geom = models.PointField()
    history = HistoricalRecords()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Development Plan"

    def __str__(self):
        return u"Dev - %s - %s (%s)" % (self.plan_name, self.devplan_id, self.submitted)

    developmentplan_mapping = {
        'objectid': 'OBJECTID',
        'devplan_id': 'devplan_id',
        'submitted': 'submitted',
        'submitted_field': 'submitted_',
        'approved': 'approved',
        'daystoappr': 'daystoappr',
        'plan_type': 'plan_type',
        'status': 'status',
        'appealperi': 'appealperi',
        'updated': 'updated',
        'sunset_dat': 'sunset_dat',
        'acreage': 'acreage',
        'major_stre': 'major_stre',
        'cac': 'cac',
        'engineer': 'engineer',
        'engineer_p': 'engineer_p',
        'developer': 'developer',
        'developer_field': 'developer_',
        'plan_name': 'plan_name',
        'planurl': 'planurl',
        'planurl_ap': 'planurl_ap',
        'planner': 'planner',
        'lots_req': 'lots_req',
        'lots_rec': 'lots_rec',
        'lots_apprv': 'lots_apprv',
        'sq_ft_req': 'sq_ft_req',
        'units_appr': 'units_appr',
        'units_req': 'units_req',
        'zoning': 'zoning',
        'plan_numbe': 'plan_numbe',
        'creationda': 'CreationDa',
        'creator': 'Creator',
        'editdate': 'EditDate',
        'editor': 'Editor',
        'geom': 'POINT',
    }


class SiteReviewCases(models.Model):
    # A Site Review Case is an item on the Development Activity page - Site Review Cases (SR) section
    case_number = models.CharField(blank=True, max_length=100, null=True, verbose_name="Case Number")
    case_url = models.TextField(blank=True, null=True, verbose_name="Plan URL")
    project_name = models.CharField(blank=True, max_length=300, null=True, verbose_name="Plan Name")
    cac = models.CharField(blank=True, max_length=100, null=True, verbose_name="CAC")
    cac_override = models.CharField(blank=True, max_length=100, null=True, verbose_name="CAC Override")
    status = models.CharField(blank=True, max_length=100, null=True, verbose_name="Status")
    contact = models.CharField(blank=True, max_length=100, null=True, verbose_name="Contact")
    contact_url = models.CharField(blank=True, max_length=300, null=True, verbose_name="Contact URL")
    history = HistoricalRecords()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Review Case"

    def __str__(self):
        return u"SR - %s - %s (%s)" % (self.case_number, self.project_name, self.cac)


class Zoning(models.Model):
    # Zoning is an item produced by the Zoning API
    OBJECTID = models.IntegerField(blank=True, null=True, verbose_name="Object ID")
    zpyear = models.SmallIntegerField(blank=True, null=True, verbose_name="Year Submitted")
    zpnum = models.SmallIntegerField(blank=True, null=True, verbose_name="Zoning Number")
    submittal_date = models.BigIntegerField(blank=True, null=True, verbose_name="Submitted")
    petitioner = models.CharField(blank=True, max_length=300, null=True, verbose_name="Petitioner")
    location = models.CharField(blank=True, max_length=300, null=True, verbose_name="Location")
    remarks = models.CharField(blank=True, max_length=300, null=True, verbose_name="Remarks") # API field
    zp_petition_acres = models.CharField(blank=True, max_length=100, null=True, verbose_name="Acreage") # Need to convert from decimal to char
    planning_commission_action = models.CharField(blank=True, max_length=300, null=True, verbose_name="PC Action")
    city_council_action = models.CharField(blank=True, max_length=300, null=True, verbose_name="CC Action")
    ph_date = models.BigIntegerField(blank=True, null=True, verbose_name="PH Date")
    withdraw_date = models.BigIntegerField(blank=True, null=True, verbose_name="Withdraw Date")
    exp_date_120_days = models.BigIntegerField(blank=True, null=True, verbose_name="Exp Date 120 Days")
    exp_date_2_year = models.BigIntegerField(blank=True, null=True, verbose_name="Exp Date 2 Year")
    ordinance_number = models.CharField(blank=True, max_length=300, null=True, verbose_name="Ordinance Number")
    received_by = models.CharField(blank=True, max_length=300, null=True, verbose_name="Received By")
    last_revised = models.CharField(blank=True, max_length=300, null=True, verbose_name="Last Revised")
    drain_basin = models.CharField(blank=True, max_length=300, null=True, verbose_name="Drain Basin")
    cac = models.CharField(blank=True, max_length=300, null=True, verbose_name="CAC")
    cac_override = models.CharField(blank=True, max_length=100, null=True, verbose_name="CAC Override")
    comprehensive_plan_districts = models.CharField(blank=True, max_length=300, null=True, verbose_name="Comprehensive Plan Districts")
    GlobalID = models.CharField(blank=True, max_length=300, null=True, verbose_name="Global ID")
    CreationDate = models.BigIntegerField(blank=True, null=True, verbose_name="Creation Date")
    EditDate = models.BigIntegerField(blank=True, null=True, verbose_name="Edit Date")
    history = HistoricalRecords()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(blank=True, max_length=300, null=True, verbose_name="Status") # Web scrape field
    plan_url = models.TextField(blank=True, null=True, verbose_name="Plan URL")
    location_url = models.TextField(blank=True, null=True, verbose_name="Location URL")

    class Meta:
        verbose_name = "Zoning Request"

    def __str__(self):
        return u"Zone - %s (%s)" % (self.zpnum, self.zpyear)


class AdministrativeAlternates(models.Model):
    # An Administrative Alternate is an item on the Development Activity page - Administrative Alternate Requests (AAD)
    # section
    case_number = models.CharField(blank=True, max_length=300, null=True, verbose_name="Case Number")
    case_url = models.TextField(blank=True, null=True, verbose_name="Plan URL")
    project_name = models.CharField(blank=True, max_length=300, null=True, verbose_name="Plan Name")
    cac = models.CharField(blank=True, max_length=100, null=True, verbose_name="CAC")
    cac_override = models.CharField(blank=True, max_length=100, null=True, verbose_name="CAC Override")
    status = models.CharField(blank=True, max_length=300, null=True, verbose_name="Status")
    contact = models.CharField(blank=True, max_length=300, null=True, verbose_name="Contact")
    contact_url = models.CharField(blank=True, max_length=300, null=True, verbose_name="Contact URL")
    history = HistoricalRecords()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Administrative Alternate Request"

    def __str__(self):
        return u"AAR - %s - %s (%s)" % (self.case_number, self.project_name, self.cac)


class TextChangeCases(models.Model):
    # A text change case is an item on the Development Activity page - Text Change Cases (TC) section
    case_number = models.CharField(blank=True, max_length=100, null=True, verbose_name="Case Number")
    case_url = models.TextField(blank=True, null=True, verbose_name="Plan URL")
    project_name = models.CharField(blank=True, max_length=300, null=True, verbose_name="Plan Name")
    status = models.CharField(blank=True, max_length=100, null=True, verbose_name="Status")
    contact = models.CharField(blank=True, max_length=100, null=True, verbose_name="Contact")
    contact_url = models.CharField(blank=True, max_length=300, null=True, verbose_name="Contact URL")
    history = HistoricalRecords()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Text Change Case"

    def __str__(self):
        return u"TCC - %s - %s" % (self.case_number, self.project_name)
