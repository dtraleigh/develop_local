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
        # Need to create a few SRs
        SiteReviewCases.objects.create(case_number="Test-SR-2020",
                                       cac="Central",
                                       cac_override=None,
                                       project_name="Test SR Project")
        SiteReviewCases.objects.create(case_number="Test-SR-2020",
                                       cac="Central",
                                       cac_override="South Central",
                                       project_name="Test SR Project")
        SiteReviewCases.objects.create(case_number="Test-SR-2020",
                                       cac=None,
                                       cac_override="South Central",
                                       project_name="Test SR Project")
        SiteReviewCases.objects.create(case_number="Test-SR-2020",
                                       cac=None,
                                       cac_override=None,
                                       project_name="Test SR Project")

    def test_add_debug_text(self):
        all_test_items = SiteReviewCases.objects.all()
        for item in all_test_items:
            if settings.DEVELOP_INSTANCE == "Develop":
                self.assertNotEqual(add_debug_text(item), "")
            else:
                self.assertEqual(add_debug_text(item), "")
