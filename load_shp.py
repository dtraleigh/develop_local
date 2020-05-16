import os
from django.contrib.gis.utils import LayerMapping
from develop.models import CitizenAdvisoryCouncil, WakeCorporate, WakeTownship

citizenadvisorycouncil_mapping = {
    'objectid': 'OBJECTID',
    'cac': 'CAC',
    'name': 'NAME',
    'cac_code': 'CAC_CODE',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}

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

waketownship_mapping = {
    'objectid': 'OBJECTID',
    'ftr_code': 'FTR_CODE',
    'township': 'TOWNSHIP',
    'name': 'NAME',
    'geom': 'MULTIPOLYGON',
}

cac_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Citizen_Advisory_Council', 'Citizen_Advisory_Council.shp'),
)

wake_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Corporate_Limits', 'Corporate_Limits.shp'),
)

wake_twnshp_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Townships-shp',
                 '01364030-cddb-4670-a095-4e15193665872020330-1-d3s0ym.2yd2o.shp'),
)


def run_cac(verbose=True):
    lm = LayerMapping(CitizenAdvisoryCouncil, cac_shp, citizenadvisorycouncil_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


def run_wake(verbose=True):
    lm = LayerMapping(WakeCorporate, wake_shp, wakecorporate_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


def run_wake_twnshp(verbose=True):
    lm = LayerMapping(WakeTownship, wake_twnshp_shp, waketownship_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
