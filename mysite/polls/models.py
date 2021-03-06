from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import timedelta
from mongoengine import *

connect('python')
class MyUser(Document):
    username = StringField(max_length=30)
    password = IntField(required=True)

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date > (timezone.now() - timedelta(days=1))

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published Recently?"

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text


class Country(models.Model):
    CHOICES = (
        (1, 'China'),
        (2, 'USA'),
        (3, 'UN')
    )
    country = models.CharField(choices=CHOICES, null=False, max_length=128)