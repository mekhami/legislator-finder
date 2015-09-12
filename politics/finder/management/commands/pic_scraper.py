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

def scrape_congress_image_url(firstname, lastname, bioguide):
    page = requests.get('https://www.congress.gov/member/{}-{}/{}'.format(firstname, lastname, bioguide))
    soup = BeautifulSoup(page.text, "html.parser")
    img = soup.find('div', attrs={'class': 'member_picture'}).a.get('href')
    return 'https://www.congress.gov/{}'.format(img)

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
                        'congress_image_url': scrape_congress_image_url(leg['first_name'],
                                                                        leg['last_name'],
                                                                        leg['bioguide_id']),
                        'twitter_image_url': scrape_twitter_url(leg['twitter_id']),
                        }
                    )
                if created:
                    print("Created a new entry for {} {}".format(leg['first_name'], leg['last_name']))
                else:
                    print("Updating image urls for {} {}".format(leg['first_name'], leg['last_name']))
                    obj.twitter_image_url = scrape_twitter_url(leg['twitter_id'])
                    omg.congress_image_url = scrape_congress_image_url(leg['first_name'],
                                                                       leg['last_name'],
                                                                       leg['bioguide_id'])
                    obj.save()

            except KeyError:
                print("No twitter information found for {}".format(leg['last_name'] + leg['first_name']))
