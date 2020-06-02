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

    def test_get_new_dev_text(self):
        new_dev1 = DevelopmentPlan.objects.all()[0]
        new_dev2 = SiteReviewCases.objects.all()[0]

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_new_dev_text(new_dev1), None)
        self.assertNotEqual(get_new_dev_text(new_dev2), None)

    def test_get_updated_dev_text(self):
        new_dev1 = DevelopmentPlan.objects.all()[0]
        new_dev2 = SiteReviewCases.objects.all()[0]

        # Need to perform some update on each
        new_dev1.status = "New Status"
        new_dev1.save()
        new_dev2.status = "New Status"
        new_dev2.save()

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_updated_dev_text(new_dev1), None)
        self.assertNotEqual(get_updated_dev_text(new_dev2), None)

    def test_get_new_zon_text(self):
        new_zon1 = Zoning.objects.all()[0]

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_new_zon_text(new_zon1), None)

    def test_get_updated_zon_text(self):
        new_zon1 = Zoning.objects.all()[0]

        # Need to perform some update on each
        new_zon1.status = "New Status"
        new_zon1.save()

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_updated_zon_text(new_zon1), None)

    def test_get_new_aad_text(self):
        new_aad1 = AdministrativeAlternates.objects.all()[0]

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_new_aad_text(new_aad1), None)

    def test_get_updated_aad_text(self):
        new_aad1 = AdministrativeAlternates.objects.all()[0]

        # Need to perform some update on each
        new_aad1.status = "New Status"
        new_aad1.save()

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_updated_aad_text(new_aad1), None)

    def test_get_new_tc_text(self):
        new_tcc1 = TextChangeCases.objects.all()[0]

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_new_tc_text(new_tcc1), None)

    def test_get_updated_tc_text(self):
        new_tcc1 = TextChangeCases.objects.all()[0]

        # Need to perform some update on each
        new_tcc1.status = "New Status"
        new_tcc1.save()

        # We just want to know we don't get None or an assertionError when we run through these functions
        self.assertNotEqual(get_updated_tc_text(new_tcc1), None)


