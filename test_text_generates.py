from django.test import SimpleTestCase
from django.test import TestCase
from develop.management.commands.text_generates import *
from develop.test_data import *

from django.conf import settings

from develop.test_data.create_test_data import *


class TextGenTestCaseSimple(SimpleTestCase):
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


class TextGenTestCaseDjango(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_data_dev_plans()
        create_test_data_aads()
        create_test_data_zoning()
        create_test_data_site_reviews()
        create_test_data_tccs()

        # print(len(DevelopmentPlan.objects.all()))
        # print(len(SiteReviewCases.objects.all()))
        # print(len(Zoning.objects.all()))
        # print(len(AdministrativeAlternates.objects.all()))
        # print(len(TextChangeCases.objects.all()))

    def test_add_debug_text(self):
        all_test_items = SiteReviewCases.objects.all()
        for item in all_test_items:
            if settings.DEVELOP_INSTANCE == "Develop":
                self.assertNotEqual(add_debug_text(item), "")
            else:
                self.assertEqual(add_debug_text(item), "")
