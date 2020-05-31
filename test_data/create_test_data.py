from django.core import serializers


def create_test_data_dev_plans():
    # Creates 87 Dev plans that took place in 2020
    with open("develop/test_data/test_data_DevelopmentPlans.json") as jsonfile:
        for obj in serializers.deserialize("json", jsonfile):
            obj.save()


def create_test_data_site_reviews():
    # Creates 50 SRs
    with open("develop/test_data/test_data_SiteReviewCases.json") as jsonfile:
        for obj in serializers.deserialize("json", jsonfile):
            obj.save()


def create_test_data_zoning():
    # Creates 50 zoning cases
    with open("develop/test_data/test_data_Zoning.json") as jsonfile:
        for obj in serializers.deserialize("json", jsonfile):
            obj.save()


def create_test_data_aads():
    # Creates 50 AADs
    with open("develop/test_data/test_data_AdministrativeAlternates.json") as jsonfile:
        for obj in serializers.deserialize("json", jsonfile):
            obj.save()


def create_test_data_tccs():
    # Creates 24 TCCs
    with open("develop/test_data/test_data_TextChangeCases.json") as jsonfile:
        for obj in serializers.deserialize("json", jsonfile):
            obj.save()
