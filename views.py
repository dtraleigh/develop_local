from django.shortcuts import render
from django.contrib.gis.db.models.functions import AsGeoJSON
import json
from django.core.serializers import serialize
from develop.models import CitizenAdvisoryCouncil, TrackArea


def cac(request):
    cac_data = serialize("geojson", CitizenAdvisoryCouncil.objects.all(), geometry_field="geom", fields=("name",))

    return render(request, "cac.html", {"cac_data": cac_data})


def itb(request):
    itb_data = serialize("geojson", TrackArea.objects.all(), geometry_field="geom", fields=("long_name",))

    return render(request, "itb.html", {"itb_data": itb_data})
