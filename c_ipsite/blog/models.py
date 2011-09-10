from django.db import models

# Create your models here.

class Blog(models.Model):
    ime_bloga = models.CharField(max_length=100)
    opis_bloga = models.TextField()

    def __unicode__(self):
        return self.ime_bloga

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name
"""
class Comment(models.Model):
    comment_tekst = models.TextField()
    n_comment = models.IntegerField()
    comment_author_name = models.CharField(max_length=50)
    comment_author_email = models.EmailField()
"""

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    naslov = models.CharField(max_length=255)
    body_tekst = models.TextField()
    datum_objave = models.DateTimeField()
    datum_izmjene = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    # comments = models.ForeignKey(Comment)
    
    def __unicode__(self):
        return self.naslov
