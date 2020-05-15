import os
from django.contrib.gis.utils import LayerMapping
from develop.models import CitizenAdvisoryCouncil, WakeCorporate

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

cac_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Citizen_Advisory_Council', 'Citizen_Advisory_Council.shp'),
)

wake_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Corporate_Limits', 'Corporate_Limits.shp'),
)


def run_cac(verbose=True):
    lm = LayerMapping(CitizenAdvisoryCouncil, cac_shp, citizenadvisorycouncil_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


def run_wake(verbose=True):
    lm = LayerMapping(WakeCorporate, wake_shp, wakecorporate_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
