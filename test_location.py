from django.test import SimpleTestCase
from django.test import TestCase

from develop.management.commands.location import *
from develop import load_shp


class LocationSimpleTestCase(SimpleTestCase):
    def test_clean_address(self):
        address1 = "S West Street"
        self.assertEqual(clean_address(address1), "south West Street, raleigh NC USA")

        address2 = "E LENOIR ST"
        self.assertEqual(clean_address(address2), "east LENOIR ST, raleigh NC USA")

        address3 = "T W ALEXANDER  DR"
        self.assertEqual(clean_address(address3), "T W ALEXANDER DR, raleigh NC USA")

        address4 = "M E Valentine Dr"
        self.assertEqual(clean_address(address4), "M E Valentine Dr, raleigh NC USA")

        address5 = "US HWY 70"
        self.assertEqual(clean_address(address5), "US HWY 70, raleigh NC USA")

    def test_get_parcel_by_pin(self):
        pin1 = "1763323847"
        parcel = get_parcel_by_pin(pin1)

        self.assertEqual(parcel["PIN_NUM"], pin1)

    def test_get_lat_lon_by_pin(self):
        pin1 = "1703738654"
        self.assertEqual(get_lat_lon_by_pin(pin1), (35.76526123905713, -78.6364477714054))


class LocationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        load_shp.run_cac()
        load_shp.run_wake()

        # Create ITB track area
        TrackArea.objects.create(objectid=1,
                                 short_name="ITB",
                                 long_name="ITB Raleigh",
                                 geom="SRID=4326;MULTIPOLYGON (((-78.64185332157282 35.82449433431104, -78.61541746952635 35.81447235351721, -78.59447478154075 35.77966398711266, -78.60031126835604 35.76100042600255, -78.6308669934502 35.74261114366089, -78.68099211551316 35.75236356501054, -78.68030547000522 35.77743573247331, -78.66554259158931 35.81391553970967, -78.64185332157282 35.82449433431104)))"
                                 )

    def test_get_itb_items(self):
        # Test zoning
        # 1. Zoning case 1 is in, 2 is out.
        # zoning with cac=None, cac_override=None
        zon1 = Zoning.objects.create(OBJECTID=1,
                              zpyear=2020,
                              zpnum=14,
                              location_url="https://maps.raleighnc.gov/iMAPS/?pin=1703886253")

        zon2 = Zoning.objects.create(OBJECTID=2,
                                     zpyear=2020,
                                     zpnum=15,
                                     location_url="https://maps.raleighnc.gov/iMAPS/?pin=1706662849")

        self.assertEqual(get_itb_items([zon1, zon2]), [zon1])

        # 2. Zoning case 1 is in, 2 is out.
        # zoning with cac=value, cac_override=None
        zon1.cac = "Central"
        zon1.save()
        zon2.cac = "North"
        zon2.save()

        self.assertEqual(get_itb_items([zon1, zon2]), [zon1])

        # 3. Zoning case 1 is in, 2 is out.
        # zoning with cac=None, cac_override=value
        zon1.cac = None
        zon1.cac_override = "Central"
        zon1.save()
        zon2.cac = None
        zon2.cac_override = "North"
        zon2.save()

        self.assertEqual(get_itb_items([zon1, zon2]), [zon1])

        # 4. Add an AAD
        tcc1 = TextChangeCases.objects.create(case_number="Test-TCC-2020",
                                              project_name="Test TCC project")

        self.assertEqual(get_itb_items([zon1, zon2, tcc1]), [zon1, tcc1])

        # 5. Let's add SRs and AADs to the mix
        sr1 = SiteReviewCases.objects.create(case_number="Test-SR-2020",
                                             project_name="Test SR Project")
        aad1 = AdministrativeAlternates.objects.create(case_number="Test-AAD-2020",
                                                       project_name="Test AAD Project")

        self.assertEqual(get_itb_items([zon1, zon2, tcc1, sr1, aad1]), [zon1, tcc1])

        # 6. sr and aad have cac in
        sr1.cac = "Central"
        sr1.save()
        aad1.cac = "Central"
        aad1.save()
        self.assertEqual(get_itb_items([zon1, zon2, tcc1, sr1, aad1]), [zon1, tcc1, sr1, aad1])

        # 7. sr and aad have cac out
        sr1.cac = "North"
        sr1.save()
        aad1.cac = "North"
        aad1.save()
        self.assertEqual(get_itb_items([zon1, zon2, tcc1, sr1, aad1]), [zon1, tcc1])

        # 8. sr and aad have cac_override out
        sr1.cac_override = "North"
        sr1.save()
        aad1.cac_override = "North"
        aad1.save()
        self.assertEqual(get_itb_items([zon1, zon2, tcc1, sr1, aad1]), [zon1, tcc1])

        # 9. sr and aad have cac_override out
        sr1.cac = None
        sr1.cac_override = "North"
        sr1.save()
        aad1.cac = None
        aad1.cac_override = "North"
        aad1.save()
        self.assertEqual(get_itb_items([zon1, zon2, tcc1, sr1, aad1]), [zon1, tcc1])

    def test_cac_lookup(self):
        # Address outside of Raleigh
        the_biltmore = "1 Lodge Street, Asheville, NC 28803"
        self.assertEqual(cac_lookup(the_biltmore), None)

        # Made up address
        nowhere = "123 Nowhere actually drive"
        self.assertEqual(cac_lookup(nowhere), None)

        south_central_addr = "208 Freeman St"
        self.assertEqual(cac_lookup(south_central_addr), "South Central")

        the_pit = "328 W Davie St"
        self.assertEqual(cac_lookup(the_pit), "Central")

        generates_none = "3020, 3060, 3061, 3100 Hodge Rd"
        self.assertEqual(cac_lookup(generates_none), None)

    def test_get_cac_location(self):
        # Point in Central CAC
        cac1 = get_cac_location(35.7765539, -78.6427196)
        self.assertEqual(cac1.name, "Central")

        # Point outside Raleigh
        cac2 = get_cac_location(35.7847746, 78.4949552)
        self.assertEqual(cac2, None)

    def test_get_wake_location(self):
        # Point in Raleigh
        town1 = get_wake_location(35.7765539, -78.6427196)
        self.assertEqual(town1.long_name.lower(), "raleigh")

        # Point in Cary
        town2 = get_wake_location(35.7913298, -78.7582525)
        self.assertEqual(town2.long_name.lower(), "cary")

        # Point outside Wake
        town3 = get_wake_location(35.7847746, 78.4949552)
        self.assertEqual(town3, None)

    def test_is_itb(self):
        # Point in Raleigh
        place_in_itb = is_itb(35.7765539, -78.6427196)
        self.assertEqual(place_in_itb, True)

        # Point in Cary
        place_not_in_itb = is_itb(35.7913298, -78.7582525)
        self.assertEqual(place_not_in_itb, False)

        # bogus data
        weird_place = is_itb(-350.7913298, 780.7582525)
        self.assertEqual(weird_place, False)

    def test_calculate_cac(self):
        url1 = "https://maps.raleighnc.gov/iMAPS/?pin=0772865947"
        self.assertEqual(calculate_cac(url1), "West")

        url2 = "https://maps.raleighnc.gov/iMAPS/?pin=0772865947,0772875055,0772875125,0772873120"
        self.assertEqual(calculate_cac(url2), "West")

        url3 = "https://maps.raleighnc.gov/iMAPS/?pin=1703569731"
        self.assertEqual(calculate_cac(url3), "Central")

        url4 = "https://maps.raleighnc.gov/iMAPS/?pin= 1703569731"
        self.assertEqual(calculate_cac(url4), "Central")

        url5 = "https://maps.raleighnc.gov/iMAPS/"
        self.assertEqual(calculate_cac(url5), None)

        url6 = ""
        self.assertEqual(calculate_cac(url6), None)

        url7 = None
        self.assertEqual(calculate_cac(url7), None)

    def test_get_pins_from_location_url(self):
        url1 = "https://maps.raleighnc.gov/iMAPS/?pin=0772865947"
        self.assertEqual(get_pins_from_location_url(url1), ["0772865947"])

        url2 = "https://maps.raleighnc.gov/iMAPS/?pin=0772865947,0772875055,0772875125,0772873120"
        self.assertEqual(get_pins_from_location_url(url2), ["0772865947", "0772875055", "0772875125", "0772873120"])

        url3 = "https://maps.raleighnc.gov/iMAPS/?pin=1703569731"
        self.assertEqual(get_pins_from_location_url(url3), ["1703569731"])

        url4 = "https://maps.raleighnc.gov/iMAPS/?pin= 1703569731"
        self.assertEqual(get_pins_from_location_url(url4), ["1703569731"])

        url5 = "https://maps.raleighnc.gov/iMAPS/"
        self.assertEqual(get_pins_from_location_url(url5), None)

        url6 = ""
        self.assertEqual(get_pins_from_location_url(url6), None)

        url7 = None
        self.assertEqual(get_pins_from_location_url(url7), None)
