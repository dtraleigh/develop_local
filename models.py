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
    devplan_id = models.IntegerField(blank=True, null=True)
    submitted = models.DateField(blank=True, null=True)
    submitted_field = models.IntegerField(blank=True, null=True)
    approved = models.DateField(blank=True, null=True)
    daystoappr = models.IntegerField(blank=True, null=True)
    plan_type = models.CharField(max_length=39, blank=True, null=True)
    status = models.CharField(max_length=18, blank=True, null=True)
    appealperi = models.DateField(blank=True, null=True)
    updated = models.DateField(blank=True, null=True)
    sunset_dat = models.DateField(blank=True, null=True)
    acreage = models.FloatField(blank=True, null=True)
    major_stre = models.CharField(max_length=31, blank=True, null=True)
    cac = models.CharField(max_length=18, blank=True, null=True)
    engineer = models.CharField(max_length=35, blank=True, null=True)
    engineer_p = models.CharField(max_length=10, blank=True, null=True)
    developer = models.CharField(max_length=48, blank=True, null=True)
    developer_field = models.CharField(max_length=13, blank=True, null=True)
    plan_name = models.CharField(max_length=100, blank=True, null=True)
    planurl = models.CharField(max_length=107, blank=True, null=True)
    planurl_ap = models.CharField(max_length=1, blank=True, null=True)
    planner = models.CharField(max_length=30, blank=True, null=True)
    lots_req = models.IntegerField(blank=True, null=True)
    lots_rec = models.IntegerField(blank=True, null=True)
    lots_apprv = models.IntegerField(blank=True, null=True)
    sq_ft_req = models.IntegerField(blank=True, null=True)
    units_appr = models.IntegerField(blank=True, null=True)
    units_req = models.IntegerField(blank=True, null=True)
    zoning = models.CharField(max_length=34, blank=True, null=True)
    plan_numbe = models.CharField(max_length=15, blank=True, null=True)
    creationda = models.DateField(blank=True, null=True)
    creator = models.CharField(max_length=12, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)
    editor = models.CharField(max_length=12, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    history = HistoricalRecords()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Development Plan"

    def __str__(self):
        return u"Dev - %s - %s (%s)" % (self.plan_name, self.devplan_id, self.submitted)

    # Model field: JSON field
    developmentplan_mapping = {
        'objectid': 'OBJECTID',
        'devplan_id': 'devplan_id',
        'submitted': 'submitted',
        'submitted_field': 'submitted_yr',
        'approved': 'approved',
        'daystoappr': 'daystoapprove',
        'plan_type': 'plan_type',
        'status': 'status',
        'appealperi': 'appealperiodends',
        'updated': 'updated',
        'sunset_dat': 'sunset_date',
        'acreage': 'acreage',
        'major_stre': 'major_street',
        'cac': 'cac',
        'engineer': 'engineer',
        'engineer_p': 'engineer_phone',
        'developer': 'developer',
        'developer_field': 'developer_phone',
        'plan_name': 'plan_name',
        'planurl': 'planurl',
        'planurl_ap': 'planurl_approved',
        'planner': 'planner',
        'lots_req': 'lots_req',
        'lots_rec': 'lots_rec',
        'lots_apprv': 'lots_apprv',
        'sq_ft_req': 'sq_ft_req',
        'units_appr': 'units_appr',
        'units_req': 'units_req',
        'zoning': 'zoning',
        'plan_numbe': 'plan_number',
        'creationda': 'CreationDate',
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
    zpyear = models.SmallIntegerField(blank=True, null=True, verbose_name="Year Submitted")
    zpnum = models.SmallIntegerField(blank=True, null=True, verbose_name="Zoning Number")
    location = models.CharField(blank=True, max_length=300, null=True, verbose_name="Location")
    location_url = models.TextField(blank=True, null=True, verbose_name="Location URL")
    status = models.CharField(blank=True, max_length=300, null=True, verbose_name="Status") # Web scrape field
    plan_url = models.TextField(blank=True, null=True, verbose_name="Plan URL")
    received_by = models.CharField(blank=True, max_length=300, null=True, verbose_name="Received By")
    history = HistoricalRecords()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Zoning Request"

    def __str__(self):
        return u"Zone - %s (%s)" % (self.zpnum, self.zpyear)

    @property
    def short_location_url(self):
        if self.location_url:
            return self.location_url if len(self.location_url) < 35 else (self.location_url[:33] + '..')

    @property
    def short_plan_url(self):
        if self.plan_url:
            return self.plan_url if len(self.plan_url) < 35 else (self.plan_url[:33] + '..')


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
