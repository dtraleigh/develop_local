import logging

from django.core.management.base import BaseCommand
from datetime import datetime

from .emails import *

logger = logging.getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
        n = datetime.now()
        logger.info(n.strftime("%H:%M %m-%d-%y") + ": Trying to send email to admins")
        message = "Email from test_email.py"
        print("1")
        send_email_notice(message, email_admins())
        print("2")
        e = datetime.now()
        logger.info(e.strftime("%H:%M %m-%d-%y") + ": Sent test email to admins")
