from django.test import SimpleTestCase
from develop.management.commands.api_scans import *


class APIScansTestCase(SimpleTestCase):
    def test_is_current_dev(self):
        year1 = 1999
        self.assertEqual(is_current_dev(year1), False)

        year2 = 2000
        self.assertEqual(is_current_dev(year2), False)

        year3 = 2001
        self.assertEqual(is_current_dev(year3), True)

        year4 = None
        self.assertEqual(is_current_dev(year4), False)