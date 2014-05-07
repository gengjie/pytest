from django.db import models
from datetime import datetime
from datetime import timedelta
# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date > (datetime.now() - timedelta(days=1))

    was_published_recently.boolean = True
    was_published_recently.short_description = "Published Recently?"

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text