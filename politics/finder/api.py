import sunlight
from sunlight import congress

from politics import settings

sunlight.config.API_KEY = settings.SUNLIGHT_API

def query_api(zipcode):
    return congress.locate_legislators_by_zip(str(zipcode))

