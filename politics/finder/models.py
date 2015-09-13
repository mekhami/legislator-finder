from django.db import models


VOTE_CHOICES = (
        ('Yea', 'Yea'),
        ('Nay', 'Nay'),
        ('Not Voting', 'Not Voting'),
        ('Not Present', 'Not Present'),
    )

CHAMBER_CHOICES = (
        ('h', 'House'),
        ('s', 'Senate'),
    )

# Create your models here.
class Legislator(models.Model):
    bioguide_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    congress_image_url = models.URLField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Bill(models.Model):
    title = models.CharField(max_length=512)
    short_title = models.CharField(max_length=200, null=True)
    number = models.IntegerField()
    chamber = models.CharField(choices=CHAMBER_CHOICES, max_length=1)
    bill_type = models.CharField(max_length=16)
    bill_id = models.CharField(max_length=20, unique=True)
    opencongress_url = models.URLField()
    sponsor = models.ForeignKey('Legislator')

    def __str__(self):
        if self.short_title:
            return self.short_title
        else:
            return self.title


class Vote(models.Model):
    bill = models.ForeignKey('Bill')
    legislator = models.ForeignKey('Legislator')
    vote = models.CharField(choices=VOTE_CHOICES, max_length=12, default="Not Present")

    def __str__(self):
        return "{} votes {} on {}".format(self.legislator, self.vote, self.bill)
