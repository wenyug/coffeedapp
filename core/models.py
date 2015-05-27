from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField

import os
import uuid

RATING_CHOICES = (
    (0, 'None'),
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
    )

YESNO_CHOICES = (
 (0, 'First Summer'),
 (1, '1-3 years'),
 (2, '3-5 years'),
 (3, '5 + years'),
 )

PLURAL_CHOICES = (
 (0, '$.75-$1.00/min'),
 (1, '$1.00-$1.25/min'),
 (2, '$1.25-$1.50/min'),
 (3, '$1.50-$1.75/min'),
 (4, '$1.75+/min')
 )

WIFI_CHOICES = (
 (0, 'Yes'),
 (1, 'No'),
 )

COFFEE_CHOICES = (
 (0, 'Today'),
 (1, 'Next 3 Days'),
 (2, 'Next Week'),
 )

# Create your models here.

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

class Location(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    position = GeopositionField(null=True, blank=True)
    hours = models.TextField(null=True, blank=True)
    image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)
    Mow = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    Trim = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    Edge = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    Scoop_Poop = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    Responsiveness = models.IntegerField(choices=COFFEE_CHOICES, null=True, blank=True)
    Experience = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    Custom_Patterns = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    Rate = models.IntegerField(choices=PLURAL_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse(viewname="location_list", args=[self.id])

    def get_average_rating(self):
        average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
        if average == None:
            return average
        else:
            return int(average)
            
    def get_reviews(self):
        return self.review_set.all()

class Review(models.Model):
    location = models.ForeignKey(Location)
    user = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



