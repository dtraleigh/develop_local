import os
from django.contrib.gis.utils import LayerMapping
from develop.models import CitizenAdvisoryCouncil, WakeCorporate, DevelopmentPlan

citizenadvisorycouncil_mapping = {
    "objectid": "OBJECTID",
    "cac": "CAC",
    "name": "NAME",
    "cac_code": "CAC_CODE",
    "shape_leng": "SHAPE_Leng",
    "shape_area": "SHAPE_Area",
    "geom": "MULTIPOLYGON",
}

wakecorporate_mapping = {
    "objectid": "OBJECTID",
    "short_name": "SHORT_NAME",
    "long_name": "LONG_NAME",
    "ordinance_field": "ORDINANCE_",
    "effective_field": "EFFECTIVE_",
    "shapearea": "SHAPEAREA",
    "shapelen": "SHAPELEN",
    "geom": "MULTIPOLYGON",
}

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

cac_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "Citizen_Advisory_Council", "Citizen_Advisory_Council.shp"),
)

wake_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "Corporate_Limits", "Corporate_Limits.shp"),
)

devs_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "Development_Plans-shp", "Development_Plans.shp"),
)


def run_cac(verbose=True):
    lm = LayerMapping(CitizenAdvisoryCouncil, cac_shp, citizenadvisorycouncil_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


def run_wake(verbose=True):
    lm = LayerMapping(WakeCorporate, wake_shp, wakecorporate_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


def run_devs(verbose=True):
    lm = LayerMapping(DevelopmentPlan, devs_shp, developmentplan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
