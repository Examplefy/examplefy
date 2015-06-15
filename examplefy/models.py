from django.db import models

class Example(models.Model):
    title = models.CharField(max_length = 50)
    url   = models.TextField()
    def __unicode__(self):
        return unicode(self.title)
