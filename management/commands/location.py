import logging, requests, geopy
from datetime import datetime
from geopy.geocoders import Nominatim

from django.contrib.gis.geos import Point
from develop.models import *
from develop.management.commands.emails import *

logger = logging.getLogger("django")

# Testing notes
# Everything but get_subscribers_covered_CACs() and get_subscribers_covered_changed_items()
# should be covered. They will likely change soon.


def get_subscribers_covered_CACs(subscriber):
    # Subscribers have "cover areas"
    # A cover area is a collection of CACs
    # CACs should match the name of the strings coming in from the CAC field
    covered_CACs_total_extend = []
    cover_areas_for_this_user = [a for a in subscriber.cover_areas.all()]

    for area in cover_areas_for_this_user:
        cacs = [b for b in area.CACs.all()]
        covered_CACs_total_extend.extend(cacs)

    return list(set(covered_CACs_total_extend))


def get_subscribers_covered_changed_items(items_that_changed, covered_CACs_total):
    # With a subscriber's covered CACs and a list of changed items,
    # return a subset of the items that are equal to one of these CACs
    # also include CAC of None
    covered_items = []

    for item in items_that_changed:
        if isinstance(item, TextChangeCases):
            covered_items.append(item)
        else:
            try:
                if item.cac is None and item.cac_override is None:
                    covered_items.append(item)
                elif item.cac_override:
                    for cac in covered_CACs_total:
                        if cac.name.lower() in item.cac_override.lower():
                            covered_items.append(item)
                else:
                    for cac in covered_CACs_total:
                        if cac.name.lower() == item.cac.lower():
                            covered_items.append(item)

            except AttributeError:
                n = datetime.now()
                logger.info(n.strftime("%H:%M %m-%d-%y") + ": AttributeError. cac.name: " + str(cac) +
                            ", item.cac: " + str(item.cac))

    return covered_items


def get_itb_items(items_that_changed):
    # For zoning requests, we want only want the ones that are itb
    # tracked_items = []
    #
    # for item in items_that_changed:
    #     if isinstance(item, Zoning):
    #         #
    pass


def cac_lookup(address):
    # address is just a number and street name
    locator = Nominatim(user_agent="myGeocoder")

    if address:
        address = clean_address(address)  # this will append "Raleigh NC USA"
        try:
            location = locator.geocode(address)
        except geopy.exc.GeocoderTimedOut:
            return None

        if location:
            cac = get_cac_location(location.latitude, location.longitude)
            return cac.name
        else:
            n = datetime.now()
            logger.info(n.strftime("%H:%M %m-%d-%y") + ": Address could not be geocoded.")
            return None


def clean_address(address):
    """
    We need to clean the addresses a bit.
    Scenario 1: "S West St" needs to be "South West St"
    Scenario 2: "200 S West St" needs to be "200 South west St"
    Scenario 3: Need to add city, state, and country
    """
    address_parts = address.split()

    # There are a couple exceptions
    # "T W ALEXANDER  DR"
    # "M E Valentine Dr"
    if not address_parts[0].lower() == "t" and not address_parts[1].lower() == "w" and \
            not address_parts[0].lower() == "m" and not address_parts[1].lower() == "e":
        for i, part in enumerate(address_parts):
            if part.lower() == "s":
                address_parts[i] = "south"
            elif part.lower() == "n":
                address_parts[i] = "north"
            elif part.lower() == "w":
                address_parts[i] = "west"
            elif part.lower() == "e":
                address_parts[i] = "east"

    return " ".join(address_parts) + ", raleigh NC USA"


def get_wake_location(lat, lon):
    """
    Take in a lat and lon and check which muni it is in
    """
    pnt = Point(lon, lat)
    try:
        return WakeCorporate.objects.get(geom__intersects=pnt)
    except:
        return None


def get_cac_location(lat, lon):
    """
    Take in a lat and lon and check which cac it is in
    """
    pnt = Point(lon, lat)
    try:
        return CitizenAdvisoryCouncil.objects.get(geom__intersects=pnt)
    except:
        return None


def is_itb(lat, lon):
    """
    Take in a lat and lon and return True if the point is inside the
    ITB Raleigh TrackArea
    """
    pnt = Point(lon, lat)
    itb = TrackArea.objects.get(short_name="ITB")

    try:
        if TrackArea.objects.get(geom__intersects=pnt) == itb:
            return True
    except TrackArea.DoesNotExist:
        return False


def get_lat_lon_by_pin(pin):
    # This uses the County's address point API and given a pin, we return the x (lon) and y (lat) coordinates
    url = "https://maps.wakegov.com/arcgis/rest/services/Property/Addresses/MapServer/0/query?where=PIN_NUM=" + \
          str(pin) + "&outFields=*&outSR=4326&f=json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        coordinates = response.json()["features"][0]["geometry"]
        return coordinates["y"], coordinates["x"]
    return response


def get_parcel_by_pin(pin):
    # This function will use a pin and return the parcel information that comes from the county's parcel endpoint
    url = "https://maps.wakegov.com/arcgis/rest/services/Property/Parcels/MapServer/0/query?where=PIN_NUM=" + \
        pin + "&outFields=*&returnGeometry=false&outSR=4326&f=json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()["features"][0]["attributes"]
    return response


def get_pins_from_location_url(location_url):
    # This function takes in a location_url. We use the location_url string, extract the pins, and return them.
    if location_url:
        try:
            return location_url.replace(" ", "").split("=")[1].split(",")
        except IndexError:
            message = "location_url"
            message += "location.calculate_cac: This url does not have pins"
            send_email_notice(message, email_admins())
            return None
    else:
        return None


def calculate_cac(location_url):
    # This function takes in a location_url. Using get_pins_from_location_url(), we take the first pin and pass it into
    # get_parcel_by_pin(). Using the address from the json, we can use cac_lookup()
    # Ex: https://maps.raleighnc.gov/iMAPS/?pin=0772865947,0772875055,0772875125,0772873120

    list_of_pins = get_pins_from_location_url(location_url)
    if list_of_pins:
        parcel_data = get_parcel_by_pin(list_of_pins[0])
    else:
        return None

    cac_name = cac_lookup(parcel_data["SITE_ADDRESS"])

    if cac_name:
        return cac_name
    else:
        message = "Location.calculate_and_update_cac: Could not calculate CAC for a zoning case."
        message += location_url
        send_email_notice(message, email_admins())
        return None
