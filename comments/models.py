from django.conf import settings
from django.db import models


# Create your models here.

class Comment(models.Model):
    page_url = models.CharField(db_index=True, max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    reply_to = models.ForeignKey('Comment', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.text
