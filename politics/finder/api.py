import sunlight
from sunlight import congress

from politics import settings

sunlight.config.API_KEY = settings.SUNLIGHT_API

def query_api(zipcode):
    return congress.locate_legislators_by_zip(str(zipcode))

def recent_votes(page):
    return congress.votes(order='voted_at', fields='voter_ids,bill', per_page=50, page=page)

def legislator_committees(bioguide):
    return congress.committees(member_ids=bioguide)
