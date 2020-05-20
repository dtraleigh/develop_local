from django.shortcuts import render
from django.contrib.gis.db.models.functions import AsGeoJSON
import json
from django.core.serializers import serialize
from develop.models import CitizenAdvisoryCouncil


def cac(request):
    # cac2 = CitizenAdvisoryCouncil.objects.annotate(json=AsGeoJSON('geom')).get(name="Central").json
    # cac2_json = json.loads(cac2)
    cac2 = serialize("geojson", CitizenAdvisoryCouncil.objects.all(), geometry_field="geom", fields=("name",))

    return render(request, 'index.html', {"data": cac2})
