from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
import requests
import sunlight

from politics import settings
from finder.models import Legislator

sunlight.config.API_KEY = settings.SUNLIGHT_API


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--bioguide',
                            type=str,
                            help="Bioguide ID for a specific representative to update",
                            dest='bioguide')

    def handle(self, *args, **options):
        if options['bioguide']:
            legs = [sunlight.congress.legislator(options['bioguide'])]
        else:
            legs = sunlight.congress.all_legislators_in_office()
        for leg in legs:
            self.create_or_update(leg)

    def create_or_update(self, leg):
        obj, created = Legislator.objects.get_or_create(
            bioguide_id=leg['bioguide_id'],
            defaults={
                'first_name': leg['first_name'],
                'last_name': leg['last_name'],
                'congress_image_url': scrape_congress_image_url(leg['first_name'],
                                                                leg['last_name'],
                                                                leg['bioguide_id']),
                }
            )
        if created:
            self.stdout.write("Created a new entry for {} {}".format(leg['first_name'],
                                                         leg['last_name']))
        else:
            self.stdout.write("Updating image url for {} {}".format(leg['first_name'], leg['last_name']))
            obj.congress_image_url = scrape_congress_image_url(leg['first_name'],
                                                               leg['last_name'],
                                                               leg['bioguide_id'])
            obj.save()

def scrape_congress_image_url(firstname, lastname, bioguide):
    page = requests.get('https://www.congress.gov/member/{}-{}/{}'.format(firstname, lastname, bioguide))
    soup = BeautifulSoup(page.text, "html.parser")
    img = soup.find('div', attrs={'class': 'member_picture'}).a.get('href')
    return 'https://www.congress.gov/{}'.format(img)
