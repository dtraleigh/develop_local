from django.core import serializers
from django.test import SimpleTestCase
from django.test import TestCase
from develop.management.commands.text_generates import *

from django.conf import settings


class ScrapeTestCase(SimpleTestCase):
    def test_get_instance_text(self):
        if settings.DEVELOP_INSTANCE == "Develop":
            self.assertEqual(get_instance_text("DEV"),
                             "[Develop - DEV]\n")
            self.assertEqual(get_instance_text(""),
                             "[Develop - ]\n")
        else:
            self.assertEqual(get_instance_text("DEV"),
                             "")
            self.assertEqual(get_instance_text(""),
                             "")


class ScrapeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creates 87 Dev plans that took place in 2020
        with open("develop/test_data/test_data_DevelopmentPlans.json") as jsonfile:
            for obj in serializers.deserialize("json", jsonfile):
                obj.save()

    def test_add_debug_text(self):
        all_test_items = SiteReviewCases.objects.all()
        for item in all_test_items:
            if settings.DEVELOP_INSTANCE == "Develop":
                self.assertNotEqual(add_debug_text(item), "")
            else:
                self.assertEqual(add_debug_text(item), "")
