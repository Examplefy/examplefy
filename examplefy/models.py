from django.db import models

# class Tag(models.Model):
#     """
#     Singleton objects representing "tags" that can be associated with
#     an example.  An example can have many tags, and tags can be heirarchical.
#
#     In general, tags should be created by superusers at the admin site.
#     """
#     name     = models.CharField(max_length=100)
#     parent   = models.ForeignKey('self', null=True, blank=True)
#
#     def __unicode__(self):
#         return unicode(self.name)

class Topic(models.Model):
    """
    Represents a high level topic.
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

class Concept(models.Model):
    """
    Represents a concept, which exists within a Topic
    """
    name = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return unicode(self.name)


class Example(models.Model):
    """
    Represents an example.  The fundamental data type for the application.
    """
    title     = models.CharField(max_length=50)
    content   = models.TextField()
    topic     = models.ForeignKey(Topic)
    concept   = models.ForeignKey(Concept)
    email     = models.CharField(max_length=100)
    link      = models.CharField(max_length=200, null=True)
    date      = models.DateField()

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ('title',)

class Answer(models.Model):
    """
    Represents a solution to an example.
    """
    example = models.ForeignKey(Example)
    content = models.TextField()

    def __unicode__(self):
        return unicode(self.title)
