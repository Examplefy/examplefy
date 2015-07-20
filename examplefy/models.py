from django.db import models

class Tag(models.Model):
    """
    Singleton objects representing "tags" that can be associated with
    an example.  An example can have many tags, and tags can be heirarchical.

    In general, tags should be created by superusers at the admin site.
    """
    name     = models.CharField(max_length=100)
    parent   = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)

class Example(models.Model):
    """
    Represents an example.  The fundamental data type for the application.
    """
    title     = models.CharField(max_length=50)
    tags      = models.ManyToManyField(Tag, blank=True)
    content   = models.TextField()

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ('title',)
