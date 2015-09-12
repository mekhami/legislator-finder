from bs4 import BeautifulSoup
import requests
from django.core.management.base import BaseCommand, CommandError
import sunlight
import selenium

from politics import settings
from finder.models import Legislator


sunlight.config.API_KEY = settings.SUNLIGHT_API

def scrape_twitter_url(handle):
    page = requests.get('http://twitter.com/{}'.format(handle))
    soup = BeautifulSoup(page.text, "html.parser")
    img = soup.find('img', attrs={'class': 'ProfileAvatar-image'}).get('src')
    return img


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_legis = sunlight.congress.all_legislators_in_office()
        for leg in all_legis:
            try:
                obj, created = Legislator.objects.get_or_create(
                    bioguide_id=leg['bioguide_id'],
                    defaults={
                        'first_name': leg['first_name'],
                        'last_name': leg['last_name'],
                        'twitter_id': leg['twitter_id'],
                        'image_url': scrape_twitter_url(leg['twitter_id']),
                        }
                    )
                if created:
                    print("Created a new entry for {} {}".format(leg['first_name'], leg['last_name']))
                else:
                    print("Updating twitter image url for {} {}".format(leg['first_name'], leg['last_name']))
                    obj.image_url = scrape_twitter_url(leg['twitter_id'])
                    obj.save()
            except KeyError:
                print("No twitter information found for {}".format(leg['last_name'] + leg['first_name']))
                obj, created = Legislator.objects.get_or_create(
                    bioguide_id=leg['bioguide_id'],
                    defaults={
                        'first_name': leg['first_name'],
                        'last_name': leg['last_name'],
                        }
                    )
