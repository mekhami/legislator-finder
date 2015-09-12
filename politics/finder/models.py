from django.db import models

# Create your models here.
class Legislator(models.Model):
    bioguide_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    congress_image_url = models.URLField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
