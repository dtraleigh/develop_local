import logging

from django.core.management.base import BaseCommand
from datetime import datetime

from .emails import *

logger = logging.getLogger("django")


class Command(BaseCommand):
    def handle(self, *args, **options):
        n = datetime.now()
        message = "Email from test_email.py"
        send_email_notice(message, email_admins())
        e = datetime.now()
        logger.info(e.strftime("%H:%M %m-%d-%y") + ": Sent test email to admins")
