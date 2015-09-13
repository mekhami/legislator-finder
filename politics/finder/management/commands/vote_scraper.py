import time
import pprint

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError, transaction

from finder.api import recent_votes
from finder.models import Legislator, Vote, Bill


class Command(BaseCommand):
    def handle(self, *args, **options):
        count = 0
        bills = []
        bill_objects = []
        vote_objects = []

        for i in range(10):
            results = recent_votes(i)
            count += len(results)
            bills.append(results)
        self.stdout.write("Appended results of the API calls")
        self.stdout.write("{} bills ready to create.".format(count))

        for entitylist in bills:
            for bill in entitylist:
                try:
                    bill_objects.append(
                        Bill(
                            title = bill['bill']['official_title'],
                            short_title = bill['bill']['short_title'],
                            number = bill['bill']['number'],
                            chamber = bill['bill']['chamber'],
                            bill_type = bill['bill']['bill_type'],
                            bill_id = bill['bill']['bill_id'],
                            opencongress_url = bill['bill']['urls']['opencongress'],
                            sponsor = Legislator.objects.get(bioguide_id=bill['bill']['sponsor_id']))
                        )
                except KeyError:
                    pass

        with transaction.atomic():
            for bill in bill_objects:
                Bill.objects.get_or_create(
                        bill_id=bill.bill_id,
                        defaults={
                            'title': bill.title,
                            'short_title': bill.short_title,
                            'number': bill.number,
                            'chamber': bill.chamber,
                            'bill_type': bill.bill_type,
                            'bill_id': bill.bill_id,
                            'opencongress_url': bill.opencongress_url,
                            'sponsor': bill.sponsor}
                        )

        self.stdout.write("{} unique bill objects found.".format(Bill.objects.count()))
        self.stdout.write("Created the Bill objects.")

        for entitylist in bills:
            for bill in entitylist:
                status = None
                for voter, vote in bill['voter_ids'].items():
                    try:
                        vote_obj = Vote(
                            bill=Bill.objects.get(bill_id=bill['bill']['bill_id']),
                            legislator=Legislator.objects.get(bioguide_id=voter),
                            vote=vote)
                    except KeyError:
                        pass
                    vote_objects.append(vote_obj)
                if status:
                    self.stdout.write(status)
            self.stdout.write("{} votes prepared so far.".format(str(len(vote_objects))))
        self.stdout.write("{} Vote objects to create".format(str(len(vote_objects))))

        with transaction.atomic():
            for vote in vote_objects:
                Vote.objects.get_or_create(
                    bill=vote.bill,
                    legislator=vote.legislator,
                    vote=vote.vote)

        self.stdout.write("Created {} Vote objects.".format(Vote.objects.count()))
