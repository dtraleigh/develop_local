from django.shortcuts import render
import requests
from django.core.serializers import serialize
from develop.models import TrackArea, coverArea
from arcgis2geojson import arcgis2geojson
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def cac(request):
    itb_cacs = coverArea.objects.get(name="Downtown")
    cac_data = serialize("geojson", itb_cacs.CACs.all(), geometry_field="geom", fields=("name",))

    return render(request, "cac.html", {"cac_data": cac_data})


@xframe_options_exempt
def itb(request):
    itb_data = serialize("geojson", TrackArea.objects.all(), geometry_field="geom", fields=("long_name",))

    return render(request, "itb.html", {"itb_data": itb_data})


@xframe_options_exempt
def ncod(request):
    url = "https://maps.raleighnc.gov/arcgis/rest/services/Planning/Overlays/MapServer/9/query?where=1%3D1&outFields=*&outSR=4326&f=json"

    payload = {}
    headers = {
        'Cookie': 'AGS_ROLES="419jqfa+uOZgYod4xPOQ8Q=="; '
                  'RAL_LB_COOKIE=!rnL6sk/bZexYn8t2/vOhTAiUV41dAo8VuvWDDvP+/uuLwL5ZCxO1BybSDFSKC8wu8VriBaDzMAvK5xA= '
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    ncod_data = arcgis2geojson(response.json())

    return render(request, "ncod.html", {"ncod_data": ncod_data})
