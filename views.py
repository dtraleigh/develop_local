from django.shortcuts import render
from django.contrib.gis.db.models.functions import AsGeoJSON
import json, requests
from django.core.serializers import serialize
from develop.models import CitizenAdvisoryCouncil, TrackArea, coverArea


def cac(request):
    itb_cacs = coverArea.objects.get(name="Downtown")
    cac_data = serialize("geojson", itb_cacs.CACs.all(), geometry_field="geom", fields=("name",))

    return render(request, "cac.html", {"cac_data": cac_data})


def itb(request):
    itb_data = serialize("geojson", TrackArea.objects.all(), geometry_field="geom", fields=("long_name",))

    return render(request, "itb.html", {"itb_data": itb_data})
