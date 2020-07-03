# ///
# This command is used to notify subscribers of changes in the last hour
# \\\
import logging
from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.utils import timezone

from develop.models import *
from .location import *
from .actions import create_email_message, create_new_discourse_post
from .emails import *

logger = logging.getLogger("django")


def get_everything_that_changed():
    # Plans to deprecate this soon as we will move away from scanning for changes in the last hour.
    ######
    # Get everything that has changed in the last hour
    everything_that_changed = []

    # Let's exclude Development changes for now as we need to review the API content due to possible changes.
    devs_that_changed = DevelopmentPlan.objects.filter(modified_date__range=[timezone.now() - timedelta(hours=1),
                                                                             timezone.now()])
    SRs_that_changed = SiteReviewCases.objects.filter(modified_date__range=[timezone.now() - timedelta(hours=1),
                                                                            timezone.now()])
    zons_that_changed = Zoning.objects.filter(modified_date__range=[timezone.now() - timedelta(hours=1),
                                                                    timezone.now()])
    AADs_that_changed = AdministrativeAlternates.objects.filter(modified_date__range=[timezone.now() -
                                                                                      timedelta(hours=1),
                                                                                      timezone.now()])
    TCs_that_changed = TextChangeCases.objects.filter(modified_date__range=[timezone.now() -
                                                                            timedelta(hours=1),
                                                                            timezone.now()])

    for dev in devs_that_changed:
        everything_that_changed.append(dev)
    for SR in SRs_that_changed:
        everything_that_changed.append(SR)
    for AAD in AADs_that_changed:
        everything_that_changed.append(AAD)
    for TC in TCs_that_changed:
        everything_that_changed.append(TC)
    for zon in zons_that_changed:
        everything_that_changed.append(zon)

    return everything_that_changed


class Command(BaseCommand):
    def handle(self, *args, **options):
        control = Control.objects.get(id=1)
        if control.notify:

            everything_that_changed = get_everything_that_changed()

            if everything_that_changed:
                # We need to filter everything_that_changed for only the cover areas that each user is subscribed to.
                # We also need to include None. Rather than pass literally everything_that_changed let's filter it
                # for each user and then send them an email.
                # Text Changes don't have a CAC so include them all which is ok since there are so few
                all_active_subscribers = Subscriber.objects.filter(send_emails=True)

                for subscriber in all_active_subscribers:
                    # Take everything_that_changed and get the items that we want to post to discourse
                    covered_items = get_itb_items(everything_that_changed)

                    # Post to discourse community
                    if covered_items and subscriber.is_bot:
                        for item in covered_items:
                            create_new_discourse_post(subscriber, item)
                            # Alert admin if CAC is None
                            if not isinstance(item, TextChangeCases) \
                                    and not isinstance(item, Zoning) \
                                    and not isinstance(item, DevelopmentPlan):
                                if not item.cac and not item.cac_override:
                                    message = "notify: Need to add a CAC to " + str(item)
                                    send_email_notice(message, email_admins())

                    # Send emails if the subscriber is not a bot
                    if covered_items and not subscriber.is_bot:
                        message = create_email_message(covered_items)
                        email_to = [subscriber.email]
                        send_email_notice(message, email_to)

                        n = datetime.now()
                        logger.info("Email sent at " + n.strftime("%H:%M %m-%d-%y"))
